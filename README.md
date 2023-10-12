# Bewise Test Task

## Описание
API, который генерирует уникальные вопросы для викторин и сохраняет в базу данных

## Технологии
- Python
- FastAPI
- SQLAlchemy + Asyncpg
- PostgreSQL
- httpx
- Pydantic + Pydantic Settings

## Установка
```bash
git clone git@github.com:RG1ee/bewise-test.git
cd bewise-test
```

## Настройка переменных окружения
```bash
cat env.sample > .env
```

## Запуск проекта
```bash
docker compose up --build -d
```
Документация
http://0.0.0.0:8000/docs

## Пример запроса
```bash
curl -X 'POST' \                                   ─╯
  'http://0.0.0.0:8000/api/questions/get_question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 20
}'
```
