import pika
import json
from src.main.services.telegram_sender import send_telegram_message

def on_message(channel, method, properties, body):
  # msg = body.decode("utf-8")
  msg = json.loads(body)
  send_telegram_message(msg["message"])

class RabbitMQConsumer:
  def __init__(self, host='localhost', port=5672, username='guest', password='guest') -> None:
    self.__host = host
    self.__port = port
    self.__username = username
    self.__password = password
    self.__queue = "my_queue"
    self.__connection = self.connect()
    self.__channel = self.channel_config()

  def connect(self):
    credentials = pika.PlainCredentials(self.__username, self.__password)
    conn_params = pika.ConnectionParameters(host=self.__host, port=self.__port, credentials=credentials)
    self.__connection = pika.BlockingConnection(conn_params)
    print("Connected to RabbitMQ:\n" + str(self.__connection))
    return self.__connection
  
  def channel_config(self):
    self.__channel = self.__connection.channel()
    self.__channel.queue_declare(
      queue=self.__queue,
      durable=True
    )

    self.__channel.basic_consume(
      queue=self.__queue,
      auto_ack=True,
      on_message_callback=on_message
    )

    return self.__channel
  
  def start(self):
    self.channel_config()
    self.__channel.start_consuming()
