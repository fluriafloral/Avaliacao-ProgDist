import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
chat = channel.queue_declare(queue='principal', durable=True)
chat1 = channel.queue_declare(queue='segundo_canal', durable=True)
chat2 = channel.queue_declare(queue='canal_do_vasco', durable=True)

queues = ['principal', 'segundo_canal', 'canal_do_vasco']

def display_messages(queue):
    print()

    count = 0
    for method, properties, body in channel.consume(queue):
        print(body)
        count += 1
        if method.delivery_tag == count:
            break

    chat_menu(queue)

def send_message(queue):
    print()

    message = input("Digite a mensagem: ")
    message = usr + " : " + message

    channel.basic_publish(
    exchange='',
    routing_key=queue,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))

    print("Mensagem enviada com sucesso!")

    chat_menu(queue)

def chat_menu(queue):
    print()

    print("Você está no chat %r" % queue)
    print("Mensagens:")
    print("1 - Listar mensagens")
    print("2 - Enviar mensagem")
    print("3 - Voltar a lista de chats")
    command = input("Comando : ")

    if command == '1':
        display_messages(queue)
    elif command == '2':
        send_message(queue)
    elif command == '3':
        list_menu()
    else:
        print()
        print("***Comando não identificado, por favor tente novamente.")
        chat_menu(queue)
    

def list_menu():
    print()

    print("Canais de chat disponíveis: ")

    channel_number = 1
    for queue in queues:
        print(channel_number, "-", queue)
        channel_number += 1
    print(channel_number, "- Voltar ao menu inicial")
    command = input("Em qual canal deseja entrar? : ")

    if (int(command) != channel_number):
        chat_menu(queues[int(command) - 1])
    elif (int(command) == channel_number):
        initial_menu()
    else:
        print()
        print("***Comando não identificado, por favor tente novamente.")
        list_menu()

def initial_menu():
    print()
    print("Olá %r!" % usr)
    print("Selecione uma opção:")
    print("1 - Listar canais de chat disponíveis")
    print("2 - Encerrar programa")
    command = input("Comando : ")

    if command == '1':
        list_menu()
    elif command == '2':
        connection.close()
        return 0
    else:
        print()
        print("***Comando não identificado, por favor tente novamente.")
        initial_menu()


print("Bem vindo!")
usr = input("Primeiro, defina seu nome de usuário : ")
initial_menu()