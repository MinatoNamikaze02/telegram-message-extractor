import os
from dotenv import load_dotenv
import json
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, ChannelPrivateError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel



load_dotenv()


api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
phone = os.getenv('phone')
username = os.getenv('username')
print(username)

async def extract_messages(phone):
    await client.start()
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code sent to you in Telegram: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    channel = input('Enter the link of ID corresponding to the channel: ')

    if channel.isdigit():
        entity = PeerChannel(int(channel))
    else:
        entity = channel

    my_channel = await client.get_entity(entity)
    limit = int(input("Enter limit (no of messages you want extracted): "))
    offset_id = 0
    all_messages = []
    total = 1

    while True:
        print("Extracting Message", total)
        try:
            history = await client(GetHistoryRequest(peer=my_channel, offset_id=offset_id, offset_date=None, add_offset=0, limit=limit, max_id=0, min_id=0, hash=0))
        except ChannelPrivateError:
            print("Entered channel is private!")
            break
        if not history.messages or total == limit:
            break
        messages = history.messages
        for message in messages:
            if(str(message.message) == 'None'):
                continue
            #extracting the sender id and message alone
            try:
                message_info = {'from_id': str(message.from_id.user_id), 'message': str(message.message)}
                all_messages.append(message_info)
            except AttributeError:
                message_info = {'from_id': None, 'message': str(message.message)}
                all_messages.append(message_info)
        
        offset_id = messages[len(messages) - 1].id
        total += 1

    print(all_messages)

    #writing to JSON
    with open('channel_messages.json', 'w') as outfile:
        json.dump(all_messages, outfile)

    

with TelegramClient(username, api_id=api_id, api_hash=api_hash) as client:
    client.loop.run_until_complete(extract_messages(phone))
