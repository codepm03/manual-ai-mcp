import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from router_graph import route_message

# === Load secrets from environment ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# === Check for missing secrets ===
missing = []
if not OPENAI_API_KEY: missing.append("OPENAI_API_KEY")
if not LANGSMITH_API_KEY: missing.append("LANGSMITH_API_KEY")
if not LANGSMITH_PROJECT: missing.append("LANGSMITH_PROJECT")
if not TELEGRAM_BOT_TOKEN: missing.append("TELEGRAM_BOT_TOKEN")

if missing:
    print(f"❌ Missing environment variables: {', '.join(missing)}")
    sys.exit(1)

# Replace this with your bot token (set in environment or directly)
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "PUT-YOUR-BOT-TOKEN-HERE")

# Handle "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to your AI partner. Ask me anything from your life or startup.")

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = route_message(user_input)  # This will call LangGraph router
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()
