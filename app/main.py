from fastapi import FastAPI, HTTPException
from routes.task import router as task_router
from app.auth import router as auth_router
from app.database import create_tables
from app.auth import get_current_user
import httpx 

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}  

@app.on_event("startup")
async def startup():
    await create_tables()

@app.get("/fetch")
async def fetch_url(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return {"status_code": response.status_code, "content": response.text[:500]}  # فقط 500 کاراکتر اول محتوا
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
