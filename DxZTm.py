import asyncio
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient , events , sync
from telethon.tl.functions.channels import InviteToChannelRequest
import os
import json
from telethon.tl.functions.messages import AddChatUserRequest

api_id ,api_hash = 1,"" # Api ID & Api Hash ! 

with open('add.json','w') as v:
    d = {'mem':[]}
    json.dump(d,v)

Bot = TelegramClient("DxZTm" , api_id , api_hash)
Bot.start()

@Bot.on(events.NewMessage(outgoing=True, pattern='Help'))
async def crazy(event):
    await event.edit('''Guide :

Send `get` to Get Users iN a Group
To Add Saved Users From Groups, Send `add @link or username` Ex : add https:// | add @dxzgroup
Send `del` To Remove Members From Database

**Good Luck 🌹**
@DxZTm''')

@Bot.on(events.NewMessage(outgoing=True,pattern='del'))
async def dele(event):
    os.remove('add.json')
    with open('add.json','w') as l:
        v = {'mem':[]}
        json.dump(v,l)
        await event.edit('Successfully Removed')

@Bot.on(events.NewMessage(outgoing=True,pattern='get'))
async def get(event):
    await event.edit('♻️')
    with open('add.json','r') as v:
        add = json.load(v)
    chat = event.chat_id
    async for user in Bot.iter_participants(chat):
            add['mem'].append(user.id)
    with open('add.json','w') as d:
        json.dump(add,d)
    await event.edit('✅')
    

@Bot.on(events.NewMessage(outgoing=True, pattern='add'))
async def crazy(event):
    if event:
        with open('add.json','r') as fg:
            add = json.load(fg)
        await event.edit('Adding Users....')
        chat = event.chat_id
        arg = event.raw_text.split(' ')
        chat = event.chat_id
        with open("add.json",'r') as vb:
            add = json.load(vb)
        try:
            await Bot(InviteToChannelRequest(arg[1],add['mem']))
        except:
            await event.edit('Im Blocked. I Can Not')
        await event.edit('Added !')
print('Bot Is Online')
Bot.run_until_disconnected()
asyncio.get_event_loop().run_forever() 
