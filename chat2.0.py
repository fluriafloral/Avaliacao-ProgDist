import pika
from usuarios_chats import usuarios_chats

usuario = None
connection = None

# Conexão com o RabbitMQ
def conecta(chat):
    global connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # Declaração da exchanges
    channel.exchange_declare(exchange=chat, exchange_type='fanout')

    return channel

# libera a conexão com o RabbitMQ
def libera():
    global connection
    if not connection == None:
        if connection.is_open:
            connection.close()
        connection = None

# Enviar uma mensagem para um chat específico
def enviar_mensagem(chat):
    print()
    mensagem = input("Digite a mensagem: ")
    mensagem = usuario + ": " + mensagem
    channel = conecta(chat)
    channel.basic_publish(exchange=chat, routing_key='', body=mensagem)
    print(f"Mensagem enviada para o chat {chat}")
    libera()
    menu_chat(chat)

# Leitura das mensagens num determinado chat
def ler_mensagens(chat):
    print()
    print(f"Aqui estão listadas as mensagens do chat {chat}")
    print("Pressione ctrl+c para voltar ao menu de opções\n")

    channel = conecta(chat)

    try:
        def callback(ch, method, properties, body):
            print(body.decode())

        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue
        # Realizar o bind entre a exchange e a fila
        channel.queue_bind(exchange=chat, queue=queue_name)
        # Registrar a função de callback
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        # Iniciar o consumo de mensagens
        channel.start_consuming()
    except KeyboardInterrupt:
        libera()
        menu_chat(chat)

# Menu de opções do chat
def menu_chat(chat):
    print()
    print(f"Você está no menu do {chat}")
    print("Opções:")
    print("1. Listar mensagens")
    print("2. Enviar mensagem")
    print("3. Voltar a lista de chats")
    opcao = input("Opção : ")

    if opcao == '1':
        ler_mensagens(chat)
    elif opcao == '2':
        enviar_mensagem(chat)
    elif opcao == '3':
        menu_lista()
    else:
        print()
        print("***Opção não identificada, por favor tente novamente.")
        menu_chat(chat)


# Verificar os chats associados ao usuário
def menu_lista():    
    print()
    chats = usuarios_chats[usuario]
    print(f"Chats associados ao usuário {usuario}:")
    for i, chat in enumerate(chats):
        print(f"{i + 1}. {chat}")
    print(f"{len(chats) + 1}. Voltar ao menu inicial")
    opcao_chat = int(input("Digite o número do chat para enviar a mensagem: "))
    if opcao_chat > 0 and opcao_chat <= len(chats):
        chat_selecionado = chats[opcao_chat - 1]
        menu_chat(chat_selecionado)
    if opcao_chat == len(chats) + 1:
        menu_inicial()
    else:
        print("Opção inválida. Por favor tente novamente.")
        menu_lista()

# Menu de opções do programa
def menu_inicial():
    print()
    print(f"Olá {usuario}")
    print("Selecione uma opção:")
    print("1. Listar canais de chat disponíveis")
    print("2. Encerrar programa")
    opcao = input("Opção : ")

    if opcao == '1':
        menu_lista()
    elif opcao == '2':
        libera()
        return 0
    else:
        print()
        print("***Opção não identificada, por favor tente novamente.")
        menu_inicial()

# Selecionar o usuário
def seleciona_usuario():
    global usuario
    usuario = input("Digite o nome do usuário: ")
    if usuario in usuarios_chats:
        menu_inicial()
    else:
        print("Usuário não encontrado. Por favor tente novamente.")
        seleciona_usuario()

# Início do programa
print("Bem vindo!")
seleciona_usuario()