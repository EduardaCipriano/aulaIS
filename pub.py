from is_wire.core import Channel, Message

#Connect to the broker

channel = Channel("amqp://guest:guest@10.10.0.91:5672")


while True:
    # Broadcast message to anyone interested (subcribed)
    message = Message()
    message.reply_to = "Eduarda"
    Nome=input("Destinatário ")
    msg=input("fala ai:")
    message.body =msg.encode('latin1')
    channel.publish(message, topic= f"Aluno.{Nome}")

