from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
async def add_user(user: dict):
    return {"message": "User added", "user": user}

@router.get("/users")
async def get_users():
    return {"message": "List of users"}

@router.put("/users/{id}")
async def update_user(id: int, user: dict):
    return {"message": "User updated", "id": id, "user": user}

@router.delete("/users/{id}")
async def delete_user(id: int):
    return {"message": "User deleted", "id": id}
