import pika

class RabbitMQClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                credentials=pika.PlainCredentials(self.username, self.password)
            )
        )
        self.channel = self.connection.channel()

    def receive_messages(self, queue, callback):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def disconnect(self):
        self.connection.close()

class Usuario:
    def __init__(self, user_id, chat):
        self.user_id = user_id
        self.chat = chat
        self.rabbitmq_client = RabbitMQClient('localhost', 5672, 'guest', 'guest')

    def receber_mensagens(self):
        self.rabbitmq_client.connect()

        def callback(ch, method, properties, body):
            print(f"Mensagem recebida do usuário {self.user_id}: {body.decode()}")

        self.rabbitmq_client.receive_messages(self.chat, callback)

        self.rabbitmq_client.disconnect()

if __name__ == '__main__':
    # Criação dos usuários
    usuario1 = Usuario('user1', 'chat1')
    usuario2 = Usuario('user2', 'chat1')
    usuario3 = Usuario('user3', 'chat2')
    # Crie mais usuários aqui

    # Interação do usuário para receber mensagens
    while True:
        print("Receber Mensagens:")
        print("1. Receber mensagens do usuário 1")
        print("2. Receber mensagens do usuário 2")
        print("3. Receber mensagens do usuário 3")
        # Adicione mais opções para os outros usuários

        choice = input("Escolha uma opção: ")

        if choice == '1':
            usuario1.receber_mensagens()
        elif choice == '2':
            usuario2.receber_mensagens()
        elif choice == '3':
            usuario3.receber_mensagens()
        # Adicione mais condições para os outros usuários

        elif choice == 'q':
            break
