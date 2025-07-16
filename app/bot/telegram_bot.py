from aiogram import Bot, Dispatcher, types, executor
from app.config import TELEGRAM_TOKEN
from app.database import SessionLocal
from app.models import Problem, Tag

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я помогу подобрать задачи с Codeforces. Используй /find для поиска.")

@dp.message_handler(commands=["find"])
async def find(message: types.Message):
    await message.answer("Введите сложность (например, 800):")

@dp.message_handler(lambda m: m.text.isdigit())
async def by_rating(message: types.Message):
    rating = int(message.text)
    session = SessionLocal()
    problems = session.query(Problem).filter(Problem.rating == rating).limit(10).all()
    if not problems:
        await message.answer("Задачи не найдены.")
    else:
        text = ""
        for p in problems:
            text += (
                f"• <b>{p.name}</b> (<a href=\"https://codeforces.com/problemset/problem/{p.contest_id}/{p.index}\">{p.contest_id}{p.index}</a>)\n"
                f"  Сложность: <b>{p.rating}</b> | Решений: <b>{p.solved_count}</b>\n\n"
            )
        await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)
    session.close()

@dp.message_handler(lambda m: m.text.startswith("тема:"))
async def by_tag(message: types.Message):
    tag_name = message.text[5:].strip()
    session = SessionLocal()
    tag = session.query(Tag).filter_by(name=tag_name).first()
    if not tag:
        await message.answer("Тематика не найдена.")
    else:
        problems = tag.problems[:10]
        text = ""
        for p in problems:
            text += (
                f"• <b>{p.name}</b> (<a href=\"https://codeforces.com/problemset/problem/{p.contest_id}/{p.index}\">{p.contest_id}{p.index}</a>)\n"
                f"  Сложность: <b>{p.rating}</b> | Решений: <b>{p.solved_count}</b>\n\n"
            )
        await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)
    session.close()

def run_bot():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    run_bot()
