import pika
import json

class RabbitMQPublisher:
  def __init__(self, host='localhost', port=5672, username='guest', password='guest') -> None:
    self.__host = host
    self.__port = port
    self.__username = username
    self.__password = password
    self.__connection = self.connect()
    self.__channel = self.__connection.channel()
    self.__exchange = "my_exchange"
    self.__routing_key = ""

  def connect(self):
    credentials = pika.PlainCredentials(self.__username, self.__password)
    conn_params = pika.ConnectionParameters(host=self.__host, port=self.__port, credentials=credentials)
    self.__connection = pika.BlockingConnection(conn_params)
    print("Connected to RabbitMQ:\n" + str(self.__connection))
    return self.__connection
  
  def send_message(self, body: dict):
    msg_properties = pika.BasicProperties(  
      content_type="application/json",
      delivery_mode=2
    )

    self.__channel.basic_publish(
      exchange=self.__exchange, 
      routing_key=self.__routing_key, 
      body=json.dumps(body),
      properties=msg_properties
    )

rabbit_mq_publisher = RabbitMQPublisher()
rabbit_mq_publisher.send_message({"message": "Outra paçoquinha!"})
