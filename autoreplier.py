import time
import os
import asyncio
from telethon import TelegramClient, events

api_id = os.environ['TELEGRAM_API_ID']
api_hash = os.environ['TELEGRAM_API_HASH']

# content of the automatic reply
message = "Добрый день!\n" \
          "\n" \
          "Данный аккаунт зарегистрирован, чтобы можно было меня найти по номеру телефона.\n" \
          "Чтобы связаться со мной, пожалуйста, пишите на основной аккаунт: @galancev\n" \
          "\n" \
          "Данное сообщение оставлено роботом-автоответчиком"


def main():
    client = TelegramClient('telegram-auto-reply', api_id, api_hash)
    client.start()

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        print(time.asctime(), '-', event)
        time.sleep(1)
        await event.respond(message)
        chat = await client.get_input_entity(event.message.from_id)
        await client.send_read_acknowledge(chat, event.message)

    print(time.asctime(), '-', 'Waiting for incoming messages...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()
