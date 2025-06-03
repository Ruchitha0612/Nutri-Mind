from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime, timedelta

router = APIRouter()

# MongoDB setup
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["nutri_mind"]
log_collection = db["daily_logs"]

class WeeklySummaryResponse(BaseModel):
    symptom_trends: str
    food_triggers: List[str]
    improvements: str
    tips: List[str]

@router.get("/get-weekly-summary/{user_id}", response_model=WeeklySummaryResponse)
async def get_weekly_summary(user_id: str):
    today = datetime.now().date()
    week_ago = today - timedelta(days=6)
    logs = await log_collection.find({
        "user_id": user_id,
        "date": {"$gte": str(week_ago), "$lte": str(today)}
    }).to_list(length=100)
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found for this user.")

    symptom_counts = {}
    food_counts = {}
    triggers = set()
    for log in logs:
        food = log.get("food_intake", "").lower()
        symptoms = log.get("digestive_symptoms", "").lower()
        if symptoms and symptoms != "none":
            for item in food.split(","):
                item = item.strip()
                if item:
                    food_counts[item] = food_counts.get(item, 0) + 1
            for word in symptoms.split(","):
                word = word.strip()
                if word:
                    symptom_counts[word] = symptom_counts.get(word, 0) + 1
            for item in food.split(","):
                if item and symptoms:
                    triggers.add(item.strip())

    symptom_trends = f"Logged symptoms: {', '.join(symptom_counts.keys()) or 'none'}"
    improvements = "Symptom frequency appears stable."
    tips = [
        "Continue to avoid foods that triggered symptoms.",
        "Increase water intake and track your mood."
    ]
    return WeeklySummaryResponse(
        symptom_trends=symptom_trends,
        food_triggers=list(triggers),
        improvements=improvements,
        tips=tips
    ) 