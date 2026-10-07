from fastapi import APIRouter

from app.models.user import User


router = APIRouter()
users: list[User] = []


@router.get("/users", response_model=list[User])
def get_users() -> list[User]:
    return users
