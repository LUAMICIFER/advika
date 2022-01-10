
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
𝐇𝐞𝐥𝐥𝐨 𝐈 𝐀𝐦🥀🎶 𝐓𝐑𝐈𝐒𝐇𝐀 𝐱 𝐌𝐔𝐒𝐈𝐂🧚‍♀️ \n𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 🥀 𝐕𝐜 𝐌𝐮𝐬𝐢𝐜 💫 𝐏𝐥𝐚𝐲𝐞𝐫 🌎 𝐁𝐨𝐭 𝐅𝐨𝐫 \n𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 ❤️ 𝐑𝐮𝐧 𝐎𝐧 🎧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 😎 𝐕𝐩𝐬 𝐒𝐞𝐫𝐯𝐞𝐫 \n⭐𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 [٭〖𓆩𝗖𝗨𝗧𝗘 𝐊𝐈𝐍𝐆 ᵀᴹ𓆪〗٭](https://t.me/BLACKSTORM_OWNER)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿🤴❱", url="https://t.me/BlackStorm_Owner")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁🌎❱", url="https://t.me/Empire_Of_Besties"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽🚩❱", url="https://t.me/Empire_Of_Besties"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩🥀❱", url="https://t.me/Masuum_bache"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝙏𝙍𝙄𝙎𝙃𝘼 𝙭 𝙈𝙐𝙎𝙄𝘾🥀 𝐎𝐧𝐥𝐢𝐧𝐞\n🌠@BlackStorm_Owner 🥀**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁❤️", url="https://t.me/Masuum_bache")
                ]
            ]
        )
   )
