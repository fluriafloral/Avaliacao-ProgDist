import pika
from usuarios_chats import usuarios_chats

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criação das exchanges
channel.exchange_declare(exchange='chat1', exchange_type='fanout')
channel.exchange_declare(exchange='chat2', exchange_type='fanout')
channel.exchange_declare(exchange='chat3', exchange_type='fanout')
channel.exchange_declare(exchange='chat4', exchange_type='fanout')
channel.exchange_declare(exchange='chat5', exchange_type='fanout')

# Função para enviar uma mensagem para um chat específico
def enviar_mensagem(chat, mensagem):
    channel.basic_publish(exchange=chat, routing_key='', body=mensagem)
    print("Mensagem enviada para o chat", chat)

# Selecionar o usuário
usuario = input("Digite o nome do usuário: ")

# Verificar os chats associados ao usuário
if usuario in usuarios_chats:
    chats = usuarios_chats[usuario]
    print(f"Chats associados ao usuário {usuario}:")
    for i, chat in enumerate(chats):
        print(f"{i + 1}. {chat}")
    opcao_chat = int(input("Digite o número do chat para enviar a mensagem: "))
    if opcao_chat > 0 and opcao_chat <= len(chats):
        chat_selecionado = chats[opcao_chat - 1]
        mensagem = input("Digite a mensagem: ")
        enviar_mensagem(chat_selecionado, mensagem)
    else:
        print("Opção inválida. Encerrando o programa.")
else:
    print("Usuário não encontrado. Encerrando o programa.")

# Fechando a conexão com o RabbitMQ
connection.close()
