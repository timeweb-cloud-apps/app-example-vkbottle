import os

from vkbottle.bot import Bot, Message

bot = Bot(token=os.environ["BOT_TOKEN"])


@bot.on.message(text=["/start", "Начать"])
async def start(message: Message) -> None:
    await message.answer("Привет! Я бот на vkbottle, запущенный в Timeweb Cloud Apps.\nКоманды: /help")


@bot.on.message(text="/help")
async def help_command(message: Message) -> None:
    await message.answer(
        "/start — приветствие\n"
        "/help — список команд\n"
        "/ping — проверка связи\n"
        "Любой другой текст я повторю."
    )


@bot.on.message(text="/ping")
async def ping(message: Message) -> None:
    await message.answer("pong")


@bot.on.message()
async def echo(message: Message) -> None:
    if message.text:
        await message.answer(message.text)


if __name__ == "__main__":
    bot.run_forever()
