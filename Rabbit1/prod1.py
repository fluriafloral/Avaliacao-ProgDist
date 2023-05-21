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

    def send_message(self, queue, message):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)

    def disconnect(self):
        self.connection.close()

class Usuario:
    def __init__(self, user_id, chat):
        self.user_id = user_id
        self.chat = chat
        self.rabbitmq_client = RabbitMQClient('localhost', 5672, 'guest', 'guest')

    def enviar_mensagem(self, message):
        self.rabbitmq_client.connect()
        self.rabbitmq_client.send_message(self.chat, message)
        self.rabbitmq_client.disconnect()

if __name__ == '__main__':
    # Criação dos usuários
    usuario1 = Usuario('user1', 'chat1')
    usuario2 = Usuario('user2', 'chat1')
    usuario3 = Usuario('user3', 'chat2')
    # Crie mais usuários aqui

    # Interação do usuário para enviar mensagens
    while True:
        print("Enviar Mensagem:")
        print("1. Enviar mensagem como usuário 1")
        print("2. Enviar mensagem como usuário 2")
        print("3. Enviar mensagem como usuário 3")
        # Adicione mais opções para os outros usuários

        choice = input("Escolha uma opção: ")

        if choice == '1':
            message = input("Digite a mensagem a ser enviada: ")
            usuario1.enviar_mensagem(message)
        elif choice == '2':
            message = input("Digite a mensagem a ser enviada: ")
            usuario2.enviar_mensagem(message)
        elif choice == '3':
            message = input("Digite a mensagem a ser enviada: ")
            usuario3.enviar_mensagem(message)
        # Adicione mais condições para os outros usuários

        elif choice == 'q':
            break
