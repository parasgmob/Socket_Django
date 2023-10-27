from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
import time
import json

class MySyncConsumer(SyncConsumer):
  def websocket_connect(self,event):
    print('websocket connected...',event)
    self.send({
      'type':'websocket.accept'
    })

  # def websocket_receive(self,event): #runs when we receive message from client side
  #   print('websocket message is received from client side...',event) #this way we receive message from client
  #   print("client message is...",event['text'] )
  #   for i in range(10):
  #     self.send({ #for application/server sending data to client group , this way we send message to client
  #       'type':'websocket.send',
  #       'text':'message sent to client from server'+ ' '+ str(i)
  #     })
  #     time.sleep(1)
  
  def websocket_receive(self,event): #runs when we receive message from client side
    print('websocket message is received from client side...',event) #this way we receive message from client
    print("client message is...",event['text'] )
    for i in range(10):
      self.send({ #for application/server sending data to client group , this way we send message to client
        'type':'websocket.send',
        'text':json.dumps({'message sent to client from server':i})  #we can only send string in text so we have to convert into str
      })
      time.sleep(1)

  def websocket_disconnect(self,event):
    print('websocket disconnected...',event)
    raise StopConsumer

#-------------------------------------------------------------------------------------------------------------------
import asyncio

class MyAsyncConsumer(AsyncConsumer):
  async def websocket_connect(self,event):
    print('websocket connected...',event)
    await self.send({
      'type':'websocket.accept'
    })

  async def websocket_receive(self,event): #runs when we receive message from client side
    print('websocket message is received from client side...',event) #this way we receive message from client
    print("client message is...",event['text'] )
    for i in range(10):
      await self.send({ #for application/server sending data to client group , this way we send message to client
        'type':'websocket.send',
        'text':'message sent to client by asynce'+ ' '+ str(i)
      })
      await asyncio.sleep(1)


  async def websocket_disconnect(self,event):
    print('websocket disconnected...',event)
    raise StopConsumer