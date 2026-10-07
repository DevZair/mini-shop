from fastapi import FastAPI

from app.routers.users import router as users_router


app = FastAPI(title="Mini Shop API")
app.include_router(users_router)


@app.get("/")
def check_status() -> dict[str, str]:
    return {"status": "ok"}
