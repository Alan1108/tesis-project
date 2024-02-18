from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from .endpoints import tag
from .endpoints import email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.router.get("/", status_code=200)
async def health_check():
    return {"msg": "Backend is working propperly"}

app.include_router(tag.router, prefix="/tag")
app.include_router(email.router, prefix="/email")


handler = Mangum(app)
