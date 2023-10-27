#Topic -- Chat App with Static group name

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync 

class MyChannelsSyncConsumer(SyncConsumer):

  def websocket_connect(self,event):
    print('websocket connetced...',event)
    print("channel layer ......",self.channel_layer) # get default channel layer from a project
    print("channel name ......",self.channel_name) # get default channel name from a project

    print(self.scope['url_route']['kwargs']['groupkaname'],"dynamic_group_name...") #property like request in view

    self.group_name = self.scope['url_route']['kwargs']['groupkaname']

    async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name ) #it is a async method so call by sync or making it async to sync we use async_to_sync  # adding a channel to anew or existing group

    self.send({
      'type':'websocket.accept',
    })


  def websocket_receive(self,event):
    print('websocket message received from client...',event)
    print('websocket message received from client...',event['text'])
    print('Type of websocket message received from client...',type(event['text']))

    #sending msg to group 
    async_to_sync(self.channel_layer.group_send) (self.group_name,{'type':'chat.message',
    'message':event['text']
    })

  def chat_message(self,event): # creating handler for chat.message type for sending data to client 
    print('event....',event)
    print('Actual data....',event['message'])
    self.send({
      'type':'websocket.send',
      'text':event['message']

    })


  def websocket_disconnect(self,event):
    print('websocket Disconnetced...',event)
    print("channel layer disconnected ......",self.channel_layer)
    print("channel name disconnected ......",self.channel_name)
    async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name) #async function
    raise StopConsumer

#===================================================================================================================

 

class MyChannelsAsyncConsumer(AsyncConsumer):

  async def websocket_connect(self,event):
    print('websocket connetced...',event)
    print("channel layer ......",self.channel_layer) # get default channel layer from a project
    print("channel name ......",self.channel_name) # get default channel name from a project
    await self.channel_layer.group_add('programmers',self.channel_name ) #it is a async method so call by sync or making it async to sync we use async_to_sync  # adding a channel to anew or existing group

    await self.send({
      'type':'websocket.accept',
    })


  async def websocket_receive(self,event):
    print('websocket message received from client...',event)
    print('websocket message received from client...',event['text'])
    print('Type of websocket message received from client...',type(event['text']))

    #sending msg to group 
    await self.channel_layer.group_send('programmers',{'type':'chat.message',
    'message':event['text']
    })

  async def chat_message(self,event): # creating handler for chat.message type for sending data to client 
    print('event....',event)
    print('Actual data....',event['message'])
    await self.send({
      'type':'websocket.send',
      'text':event['message']

    })


  async def websocket_disconnect(self,event):
    print('websocket Disconnetced...',event)
    print("channel layer disconnected ......",self.channel_layer)
    print("channel name disconnected ......",self.channel_name)
    await self.channel_layer.group_discard('programmers',self.channel_name) #async function
    raise StopConsumer
  pass