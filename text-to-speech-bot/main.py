import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from gtts import gTTS

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أرسل لي أي نص وسأحوّله إلى صوت.")

async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    tts = gTTS(text=text, lang='ar')  # صوت ذكر بالعربية
    filename = "speech.mp3"
    tts.save(filename)
    with open(filename, 'rb') as audio:
        await update.message.reply_audio(audio=audio, caption="ها هو الصوت 🎧")
    os.remove(filename)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), text_to_speech))
    app.run_polling()
