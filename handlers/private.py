
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
ððð¥ð¥ð¨ ð ðð¦ð¥ð¶ ADVIKA ð§ââï¸ \nðð®ð©ðð«ððð¬ð­ ð¥ ðð ðð®ð¬ð¢ð ð« ðð¥ðð²ðð« ð ðð¨ð­ ðð¨ð« \nððð¥ðð ð«ðð¦ â¤ï¸ ðð®ð§ ðð§ ð§ ðð«ð¢ð¯ðð­ð ð ðð©ð¬ ððð«ð¯ðð« \nâ­ï¸ððð¯ðð¥ð¨ð©ðð ðð² [Ù­ADVIKãÙ­](https://t.me/BLACKSTORM_OWNER)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â°ð¢ðð»ð²ð¿ð¤´â±", url="https://t.me/ADVIK_24")
                  ],[
                    InlineKeyboardButton(
                        "â°ð¦ðð½ð½ð¼ð¿ððâ±", url="https://t.me/"
                    ),
                    InlineKeyboardButton(
                        "â°ðð¿ð¼ðð½ð©â±", url="https://t.me/"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "â°ðð¡ðð­ ðð«ð¨ð®ð©ð¥â±", url="https://t.me/"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Support") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ADVIK\nð @ADVIK_24 ð¥**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¦ðð½ð½ð¼ð¿ðâ¤ï¸", url="https://t.me/")
                ]
            ]
        )
   )
