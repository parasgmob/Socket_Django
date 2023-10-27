#generic consumer --> WebsocketConsumer and AsyncwebsocketConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import time
import asyncio
from asgiref.sync import async_to_sync

class MyWebsocketConsumer(WebsocketConsumer):

  def connect(self):
    print("Websocket connetced...")
    print("Channel_Layer...",self.channel_layer)
    print("Channel name...",self.channel_name)
    self.group_name = self.scope['url_route']['kwargs']['groupkaname']

    async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name) #use to add channels in same group asynce he kyuki channel alyer ke function async he to sync me use karne ke liye async_to_sync use kiya he
    
    self.accept()  #to accept the connection
    #self.close()   #to reject the connection

  def receive(self,text_data=None,bytes_data=None):
    print("Message receive from client...",text_data,"byte_data",bytes_data)
    
     # to send data to client
    #self.send(bytes_data="binary data to client from server") #to send binary frame to Client

  def disconnect(self,close_code):
    print("Websocket disconnected...",close_code)
  

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

  async def connect(self):
    print("Websocket connetced...")
    await self.accept()  #to accept the connection

    #await self.close()   #to reject the connection

  async def receive(self,text_data=None,bytes_data=None):
    print("Message receive from client...",text_data,"byte_data",bytes_data)
    await self.send(text_data="Message from server to client") 
    for i in range(20):
      await self.send(text_data=str(i))#"Message from server to client") 
      await asyncio.sleep(1)
     # to send data to client
    #self.send(bytes_data="binary data to client from server") #to send binary frame to Client

  async def disconnect(self,close_code):
    print("Websocket disconnected...",close_code)
  