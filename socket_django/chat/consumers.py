from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):

  async def connect(self):
    self.room_name=self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = 'chat_%s' % self.room_name
    await self.channel_layer.group_add(self.room_group_name,self.channel_name)

    await self.accept()  # Without accepting it will disconnect client immediately after connect.
  
  async def disconnect(self, close_code):
    await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
    

  async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']
    username = text_data_json['username']
    await self.channel_layer.group_send(self.room_group_name,{'type':'chatroom_message','message':message,'username':username,})
    
  
  async def chatroom_message(self,event):
    message = event['message']

    username = event['username']

    await self.send(text_data=json.dumps({
      'message':message,'username':username,
    }))

#-------------------------------------------------------------------------------------------------------------------

from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
  def websocket_connect(self,event):
    print('websocket connected...',event)
    self.send({
      'type':'websocket.accept'
    })

  def websocket_receive(self,event): #runs when we receive message from client side
    print('websocket message is received from client side...',event) #this way we receive message from client
    print("client message is",event['text'] )
    self.send({ #for application/server sending data to client group , this way we send message to client
      'type':'websocket.send',
      'text':'message sent to client'
    })


  def websocket_disconnect(self,event):
    print('websocket disconnected...',event)
    raise StopConsumer