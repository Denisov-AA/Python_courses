import string
import pyodbc
import os.path
import shutil
import logging
import smtplib
from email.mime.text import MIMEText


# Main Settings:
INTERVAL = 3000000  # difference which should trigger notification
COEF = 0.001
DATABASE_FILE_NAME = 'ShotsHistory.mdb'
DATABASE_PASSWORD = 'ctsoft'
LOCAL_PATH = r'C:/Monitoring/'
REMOTE_PATH = r'Z:/'
PREVIOUS_RESULT_FILE_NAME = 'previous.txt'
LOG_FILE_NAME = 'monitoring.log'
LOG_LEVEL = logging.DEBUG
TUBE_SN = '129756'

# Email Settings:

# TODO: enter correct values
EMAIL_TO = 'saturn.remote.service@gmail.com'
EMAIL_FROM = 'gbuznogkb28@gmail.com'

# SMTP Settings required for sending emails
# TODO: enter correct values
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_LOGIN = 'gbuznogkb28@gmail.com'
SMTP_PASSWORD = 'saturnwatchingyou'

# Email subject
REACHED_EMAIL_SUBJECT_TEMPLATE = string.Template(
    '[Monitoring of ' + DATABASE_FILE_NAME + '] Notification: $interval scan seconds reached $times time(s)! Status: total seconds - $total_seconds, total arcs - $total_arcs'
)

# Email template
REACHED_EMAIL_BODY_TEMPLATE = string.Template('''
Hello!

This is an automatic notification. We are happy to inform you that your device has reached $interval interval $times time(s)
since the previous notification.

Current counters:
    Total Seconds: $total_seconds
    Total Arcs:    $total_arcs

Best Regards,
Notification Service
''')

# Email subject
NOT_REACHED_EMAIL_SUBJECT_TEMPLATE = string.Template(
    '[Monitoring of ' + DATABASE_FILE_NAME + '] Status: total seconds - $total_seconds, total arcs - $total_arcs'
)

# Email template
NOT_REACHED_EMAIL_BODY_TEMPLATE = string.Template('''
Hello!

This is an automatic notification.

Current counters:
    Total Seconds: $total_seconds
    Total Arcs:    $total_arcs


Best Regards,
Notification Service
''')



def get_info_from_mdb(file_name, password):
    if not os.path.exists(file_name):
        logging.critical('Database file does not exist! Exiting')
        raise FileNotFoundError
    driver = '{Microsoft Access Driver (*.mdb)}'
    connection = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(driver, file_name, password))
    cursor = connection.cursor()
    sql_query = 'SELECT [TotalScanSeconds],[TotalLargeArcCount] FROM [Tubes] WHERE TubeSerialNumber = ?'
    total_seconds, total_arcs = cursor.execute(sql_query, TUBE_SN).fetchone()
    logging.debug('Read current values from database: total_seconds = {}, total_arcs = {}'.format(total_seconds, total_arcs))
    cursor.close()
    connection.close()
    return total_seconds, total_arcs


def get_info_from_file(file_name):
    file = open(file_name)
    total_seconds = int(file.readline())
    total_arcs = int(file.readline())

    logging.debug('Read previous result from file {}: total_seconds = {}, total_arcs = {}'.format(file_name, total_seconds, total_arcs))
    return total_seconds, total_arcs


def save_info_to_file(file_name, total_seconds, total_arcs):
    with open(file_name, mode="w") as fp:
        print(total_seconds, file=fp)
        print(total_arcs, file=fp)
    logging.debug('Saved current result to file {}: total_seconds = {}, total_arcs = {}'.format(file_name, total_seconds, total_arcs))


def send_email_notification(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    smtp_object = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp_object.set_debuglevel(1)
    try:
        smtp_object.login(SMTP_LOGIN, SMTP_PASSWORD)
        logging.debug('''
        -----------------------------------------------------
            Sending email:
        -----------------------------------------------------
            + From: {}
            + To:   {}
            + Subj: {}
        -----------------------------------------------------
        {}
        '''.format(EMAIL_FROM, EMAIL_TO, subject, body))
        smtp_object.send_message(msg, from_addr=EMAIL_FROM, to_addrs=EMAIL_TO)
    except smtplib.SMTPException as error:
        logging.error('Could not send email: ' + str(error))
        raise
    else:
        logging.info('The email was successfully sent to ' + EMAIL_TO)
    finally:
        smtp_object.close()


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        filename=LOG_FILE_NAME,
        format='%(asctime)-15s: %(levelname)s:\t%(message)s'
    )

    local_db_file = os.path.join(LOCAL_PATH, DATABASE_FILE_NAME)
    remote_db_file = os.path.join(REMOTE_PATH, DATABASE_FILE_NAME)

    logging.info('''
    ==================================================================================================================
        Starting check script
        interval: {},
        Remote database file: {}
    ==================================================================================================================
    '''.format(INTERVAL, remote_db_file))

    if os.path.exists(local_db_file):
        logging.info('Removing local mdb file {} ...'.format(local_db_file))
        os.remove(local_db_file)
        logging.info("Removed.")
    logging.info('Copying database from remote share ({}) to local directory ({})..'.format(remote_db_file, local_db_file))
    shutil.copy(src=remote_db_file, dst=local_db_file)
    logging.info('Done.')

    new_total_seconds, new_total_arcs = get_info_from_mdb(local_db_file, DATABASE_PASSWORD)

    local_history_file = os.path.join(LOCAL_PATH, PREVIOUS_RESULT_FILE_NAME)
    if not os.path.exists(local_history_file):
        logging.warning('File {} with previous results does not exist, looks like it is first run..'.format(local_history_file))
        save_info_to_file(local_history_file, new_total_seconds, new_total_arcs)
    else:
        old_total_seconds, old_total_arcs = get_info_from_file(local_history_file)
        intervals_happened = int((new_total_seconds - old_total_seconds) / INTERVAL)
        logging.info('Old values: {} {}, New values: {} {}, intervals happened: {}'.format(
            old_total_seconds, old_total_arcs,
            new_total_seconds, new_total_arcs,
            intervals_happened
        ))

        vars = {
            'interval': INTERVAL * COEF,
            'times': intervals_happened,
            'total_seconds': new_total_seconds * COEF,
            'total_arcs': new_total_arcs
        }
        if intervals_happened > 0:
            logging.info('Sending interval notification')
            subject = REACHED_EMAIL_SUBJECT_TEMPLATE.substitute(vars)
            body = REACHED_EMAIL_BODY_TEMPLATE.substitute(vars)
            send_email_notification(subject, body)
            save_info_to_file(local_history_file, new_total_seconds, new_total_arcs)
        else:
            logging.info('Sending just simple counters status')
            subject = NOT_REACHED_EMAIL_SUBJECT_TEMPLATE.substitute(vars)
            body = NOT_REACHED_EMAIL_BODY_TEMPLATE.substitute(vars)
            send_email_notification(subject, body)



if __name__ == "__main__":
    main()
