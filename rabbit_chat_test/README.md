
# Rabbitmq Chat Aplication
  aplicação simple usando o rabbitmq para simular um chat
## Instruções:
  pré requisitos
  
  ter o rabbitmq instalado na maquina
  
  
  intalar a biblioteca pika para python
  
  comando para instalar a bilbioteca: pip install pika 
  
  
  Para utilizar esse programa e simular uma conversa de chat será necessario abrir varios terminais sendo cada terminal simulando uma pessoa
  No Arquivo usuarios_chats.py tem os nomes do usuarios e os nomes do chats, para utilizar o sistema será necessario utiliza-los
  
  para cada usuario que queira utilizar executar o arquivo nome.py
  
  o arquivo nome.py e usuarios_chats.py tem que estar no mesmo diretorio
  
  Todos os chats possuem 3 usuarios, cada chat é uma exchange no rabbitmq e cada usuario possui uma queue, com 10 usuarios no sistemas e 5 chats distintos temos 5     exchanges(1 para cada grupo de chat) e 10 filas (uma para cada usuario).
  É utilizado o meio fannout para enviar as mensagens, produtores enviam menssagens em fannout para as exchanges e cada usuario consome em sua propria queue(fila)
  
  os usuarios e chats estão pré definidos não sendo possivel adicionar novos usuarios ou chats no periodo da execução
 
  
