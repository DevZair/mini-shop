from fastapi import FastAPI


app = FastAPI(title="Mini Shop API")


@app.get("/")
def check_status() -> dict[str, str]:
    return {"status": "ok"}
