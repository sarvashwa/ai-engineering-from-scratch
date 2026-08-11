from fastapi import APIRouter, Depends

from src.api.dependencies import get_user_service

from src.services.user_service import UserService
from src.api.schemas.create_user_response import CreateUserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    summary="Create User",
    description="Create a new user.",
    response_model=CreateUserResponse
)
def create_user(
    name: str,
    service: UserService = Depends(get_user_service)
):
    user = service.create_user(name)
    return {"id": user.id, "name": user.name}

@router.get(
    "/{user_id}",
    summary="Get User",
    description="Retrieve a user by their ID.",
    response_model=CreateUserResponse
)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = service.get_user_by_id(user_id)
    if user is None:
        return {"message": f"User with ID {user_id} not found."}
    return {"id": user.id, "name": user.name}

@router.put(
    "/{user_id}",
    summary="Update User",
    description="Update a user's name by their ID.",
    response_model=CreateUserResponse
)
def update_user(
    user_id: int,
    name: str,
    service: UserService = Depends(get_user_service)
):
    user = service.update_user(user_id, name)
    if user is None:
        return {"message": f"User with ID {user_id} not found."}
    return {"id": user.id, "name": user.name}

@router.delete(
    "/{user_id}",
    summary="Delete User",
    description="Delete a user by their ID."
)
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    service.delete_user(user_id)
    return {"message": f"User with ID {user_id} has been deleted."}