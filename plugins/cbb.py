#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/ZoroSan110'>𝐃ᴀᴛᴛᴇʙᴀʏᴏ</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Flux'>𝐀ɴɪᴍᴇ 𝐅ʟᴜx</a>\n○ 𝐎ɴɢᴏɪɴɢ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Ongoing_Anime_Flux'>𝐎ɴɢᴏɪɴɢ 𝐅ʟᴜx</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ : <a href='https://t.me/+pFq16XDLXVM1Yzll'>𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ 𝐅ʟᴜx</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ •', url='https://t.me/Straw_Hat_Bots')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
