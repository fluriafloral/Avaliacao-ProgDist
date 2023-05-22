# Avaliacao-ProgDist
Implementação de uma aplicação de chat utilizando o RabbitMQ, para a disciplina Tópicos Especiais em Sistemas de Informação de Gestão B, ministrada pelo professor Frederico Araujo.

Universidade Federal do Rio Grande do Norte 

Instituto Metrópole Digital

Bacharelado em Técnologia da Informação

Autoria:

  Dimitri Amaral de Lima

  Pedro Henrique Teixeira e Silva
  
## Distribuição do chat e usuarios:
chat1 [usuario1, usuario3, usuario6, usuario10]

chat2 [usuario1, usuario2, usuario3, usuario5, usuario7, usuario8, usuario9, usuario10]

chat3 [usuario1,usuario3,usuario4,usuario6,usuario7,usuario8]

chat4 [usuario2,usuario3,usuario4,usuario5,usuario6,usuario9]

chat5 [usuario2,usuario3,usuario4,usuario5,usuario7,usuario8,usuario10]

## Pré-requisitos
  -Ter o rabbitmq instalado na maquina.
  
  
  -Instalar a biblioteca pika para python (comando para instalar a bilbioteca pelo terminal do linux: pip install pika).
  
  
  -Clonar este repositório.
  
## Instruções para execução:
  No terminal, acesse a pasta onde estão os arquivos e execute:
  
  python chat.py
    
  Para utilizar esse programa e simular uma conversa de chat será necessario abrir varios terminais sendo cada terminal simulando uma pessoa
  No Arquivo usuarios_chats.py tem os nomes do usuarios e os nomes do chats, para utilizar o sistema será necessario utiliza-los
  
  ## Considerações sobre a implementação
  
  Para cada usuario que queira utilizar executar o arquivo nome.py
  
  O arquivo chat.py e usuarios_chats.py tem que estar no mesmo diretorio
  
  Todos os chats possuem ao menos 4 usuarios, cada chat é uma exchange no rabbitmq e cada usuario possui uma queue, com 10 usuarios no sistemas e 5 chats distintos temos 5 exchanges(1 para cada grupo de chat) e 10 filas (uma para cada usuario).
  
  É utilizado o meio fannout para enviar as mensagens, produtores enviam menssagens em fannout para as exchanges e cada usuario consome em sua propria queue(fila)
  
  Os usuarios e chats estão pré definidos não sendo possivel adicionar novos usuarios ou chats no periodo da execução
