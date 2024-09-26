from __future__ import print_function
from is_wire.core import Channel,Subscription
import time

#Connect to the broker
channel = Channel("amqp://guest:guest@10.10.0.91:5672")

#Subcribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic= "Aluno.Eduarda")
#... subscription.subscribe(topic="Other.Topic")

while True:
    message= channel.consume()
    print(message.reply_to)
    print(message.body.decode())
    time.sleep(1)

