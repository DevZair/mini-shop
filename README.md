# Mini Shop API

Простой учебный проект на FastAPI. Доступны проверочный маршрут `GET /` и список пользователей `GET /users`.

## Запуск

Из папки `mini-shop` выполните:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

На Windows создайте окружение командой `py -m venv .venv`, а для активации используйте `.venv\Scripts\activate`.

Откройте <http://127.0.0.1:8000/>. Ответ: `{"status":"ok"}`.
Список пользователей: <http://127.0.0.1:8000/users>. Пока он пуст и возвращает `[]`.
