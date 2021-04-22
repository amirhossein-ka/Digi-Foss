from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(
    "bot",
)


@app.on_message(filters.command("start"))
async def start(client, message: Message):
    # await message.reply_text("Hello World!", reply_to_message_id=message.message_id)
    await message.reply_text("your username is :@" + str(message.from_user.username))
    # await message.reply_text("chat: " + str(message.chat))
    # await message.reply_text(str(message.reply_to_message.text))  # اطلاعات درباره پیام رپلای شده
    # await message.reply_text(str(message.photo))
    # await message.reply_to_message.pin(True, True)


@app.on_message(filters.command("unpin") | filters.regex(r"انپین"))
async def unpin_msg(c, m: Message):
    await m.reply_to_message.unpin()
    await m.reply_text("message unpinned !", reply_to_message_id=m.reply_to_message.message_id)


@app.on_message(filters.command("pin") | filters.regex(r"پین"))
async def pin_msg(c, m: Message):
    m_id = m.reply_to_message.message_id
    await m.reply_to_message.pin(True, True)
    await m.reply_text("payam pin shod !", reply_to_message_id=m_id)


@app.on_message(filters.command("id"))
async def get_id(c, m: Message):
    await m.reply_text(str(m.reply_to_message.message_id))


@app.on_message(filters.command("del"))
async def del_10(c, m: Message):
    counter = 0
    nums = m.text.split(' ')
    nums = int(nums[1])
    msg_id = m.message_id
    while counter != nums:
        if not await app.delete_messages(m.chat.id, msg_id):
            # counter += 1
            msg_id -= 1
        else:
            counter += 1
    await m.reply_text(str(counter) + "messages deleted!")




@app.on_message(filters.command("chat_id"))
async def get_cid(c, m: Message):
    await m.reply_text(str(m.chat.id))


app.run()
