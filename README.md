# Codeforces Parser & Telegram Bot

## Описание

Парсер задач Codeforces с сохранением в PostgreSQL и Telegram-бот для поиска задач по сложности и темам.

## Запуск через Docker

1. Скопируйте репозиторий и перейдите в папку проекта.
2. Установите переменные окружения в docker-compose.yml (TELEGRAM_TOKEN).
3. Запустите:

```
docker-compose up --build
```

## Использование Telegram-бота

- /start — приветствие
- /find — поиск задач по сложности
- Сообщение вида `тема:math` — подборка задач по теме
- Сообщение с числом (например, 800) — подборка задач по сложности

## Тесты

```
pytest
```

## Стек
- Python 3.11+
- PostgreSQL
- SQLAlchemy
- aiogram
- APScheduler
- Docker

## Структура
- app/ — исходный код
- tests/ — тесты
