import pika
from usuarios_chats import usuarios_chats

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Função de callback para tratar as mensagens recebidas
def callback(ch, method, properties, body):
    print("Mensagem recebida:", body.decode())

# Selecionar o usuário
usuario = input("Digite o nome do usuário: ")

# Verificar os chats associados ao usuário
if usuario in usuarios_chats:
    chats = usuarios_chats[usuario]
    print(f"Chats associados ao usuário {usuario}:")
    for i, chat in enumerate(chats):
        print(f"{i + 1}. {chat}")
    opcao_chat = int(input("Digite o número do chat para consumir as mensagens: "))
    if opcao_chat > 0 and opcao_chat <= len(chats):
        chat_selecionado = chats[opcao_chat - 1]
        # Criar a exchange e a fila
        channel.exchange_declare(exchange=chat_selecionado, exchange_type='fanout')
        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue
        # Realizar o bind entre a exchange e a fila
        channel.queue_bind(exchange=chat_selecionado, queue=queue_name)
        # Registrar a função de callback
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        # Iniciar o consumo de mensagens
        channel.start_consuming()
    else:
        print("Opção inválida. Encerrando o programa.")
else:
    print("Usuário não encontrado. Encerrando o programa.")

# Fechando a conexão com o RabbitMQ
connection.close()
