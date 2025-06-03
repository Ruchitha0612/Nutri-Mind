from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import date

router = APIRouter()

# MongoDB setup
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["nutri_mind"]
log_collection = db["daily_logs"]

class DailyLog(BaseModel):
    user_id: str = Field(...)
    date: str = Field(default_factory=lambda: str(date.today()))
    food_intake: str
    digestive_symptoms: Optional[str] = ""
    mood: Optional[str] = ""
    activity_level: Optional[str] = ""

@router.post("/daily-log", response_model=DailyLog)
async def submit_daily_log(log: DailyLog):
    await log_collection.insert_one(log.dict())
    return log

@router.get("/daily-log/{user_id}", response_model=List[DailyLog])
async def get_daily_logs(user_id: str):
    logs = await log_collection.find({"user_id": user_id}).to_list(length=100)
    for log in logs:
        log.pop("_id", None)
    return logs 