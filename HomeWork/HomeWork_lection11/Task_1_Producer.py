import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='quene_name')
for task_number in range(100):
    task_number_message = f'Your task #{task_number}'
    channel.basic_publish(exchange='', routing_key='quene_name', body=task_number_message)
    print(f" [x] Sent task №{task_number}")

connection.close()
