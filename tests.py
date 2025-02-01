import unittest
from unittest.mock import Mock, patch
from publisher import RabbitMQPublisher

class TestRabbitMQPublisher(unittest.TestCase):
    @patch('pika.BlockingConnection')
    @patch('pika.ConnectionParameters')
    @patch('pika.PlainCredentials') 
    def setUp(self, mock_credentials, mock_params, mock_connection):
        self.mock_credentials = mock_credentials
        self.mock_params = mock_params
        self.mock_connection = mock_connection
        
        self.publisher = RabbitMQPublisher()
        
        # Configurar o mock do canal
        self.mock_channel = Mock()
        self.publisher._RabbitMQPublisher__connection.channel.return_value = self.mock_channel

    def test_init_default_values(self):
        """Testa se os valores padrão são configurados corretamente no construtor"""
        self.assertEqual(self.publisher._RabbitMQPublisher__host, 'localhost')
        self.assertEqual(self.publisher._RabbitMQPublisher__port, 5672)
        self.assertEqual(self.publisher._RabbitMQPublisher__username, 'guest')
        self.assertEqual(self.publisher._RabbitMQPublisher__password, 'guest')
        self.assertEqual(self.publisher._RabbitMQPublisher__exchange, 'my_exchange')
        self.assertEqual(self.publisher._RabbitMQPublisher__routing_key, '')

    def test_connect_calls_pika_correctly(self):
        """Testa se o método connect faz as chamadas corretas para o pika"""
        self.mock_credentials.assert_called_once_with('guest', 'guest')
        self.mock_params.assert_called_once()
        self.mock_connection.assert_called_once()

    def test_send_message(self):
        """Testa se a mensagem é publicada corretamente"""
        test_message = {"test": "message"}
        self.publisher.send_message(test_message)
        
        self.mock_channel.basic_publish.assert_called_once()
        call_kwargs = self.mock_channel.basic_publish.call_args[1]
        
        self.assertEqual(call_kwargs['exchange'], 'my_exchange')
        self.assertEqual(call_kwargs['routing_key'], '')
        self.assertIn('body', call_kwargs)
        self.assertIn('properties', call_kwargs)

if __name__ == '__main__':
    unittest.main()
