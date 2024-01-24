from fastapi import APIRouter, status

router = APIRouter(
    tags=["tag"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/health_check", status_code=200)
async def health_check() -> dict:
    return {"msg": "Backend is working properly"}


@router.post("/")
async def tag_image():
    return {"msg": "not implemented yet"}
