# Mini Shop API

Простой учебный проект на FastAPI. Пока доступен только проверочный маршрут `GET /`.

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
