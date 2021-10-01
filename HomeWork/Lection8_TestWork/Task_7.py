import os


def copyfile(source, destination):
    try:
        with open(source, 'r') as file:
            data = file.read()
        if os.path.exists(destination) is True:
            pass
        else:
            raise FileNotFoundError
        with open(destination, 'w') as file:
            file.write(data)

    except FileNotFoundError:
        print('File not found')


sourse = r'C:\Users\Andrew\PycharmProjects\ControlWork\Sourse.txt'  # For example
dest = r'C:\Users\Andrew\PycharmProjects\ControlWork\Dest.txt'      # For example
copyfile(sourse, dest)
