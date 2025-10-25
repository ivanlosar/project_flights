from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.core.security import api_key_auth

router = APIRouter(tags=["users"])

_USERS: dict[str, User] = {
    "u1": User(id="u1", email="ana@example.com", name="Ana"),
    "u2": User(id="u2", email="luis@example.com", name="Luis"),
}

@router.get("/", response_model=list[User], summary="Listar usuarios")
def list_users(auth: bool = Depends(api_key_auth)):
    return list(_USERS.values())

@router.get("/{user_id}", response_model=User, summary="Obtener usuario por ID")
def get_user(user_id: str, auth: bool = Depends(api_key_auth)):
    u = _USERS.get(user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return u

@router.post("/", response_model=User, summary="Crear usuario")
def create_user(user: User, auth: bool = Depends(api_key_auth)):
    if user.id in _USERS:
        raise HTTPException(status_code=409, detail="User already exists")
    _USERS[user.id] = user
    return user
