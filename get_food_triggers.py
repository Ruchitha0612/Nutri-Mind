from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
import os
from set_meal_plan import router as meal_plan_setter_router
from get_weekly_summary import router as weekly_summary_router

router = APIRouter()

# MongoDB setup
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["nutri_mind"]
log_collection = db["daily_logs"]

class FoodTriggersResponse(BaseModel):
    triggers: List[str]

@router.get("/food-triggers/{user_id}", response_model=FoodTriggersResponse)
async def get_food_triggers(user_id: str):
    logs = await log_collection.find({"user_id": user_id}).to_list(length=100)
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found for this user.")

    trigger_counts = {}
    for log in logs:
        food = log.get("food_intake", "").lower()
        symptoms = log.get("digestive_symptoms", "").lower()
        if symptoms and symptoms != "none":
            for item in food.split(","):
                item = item.strip()
                if item:
                    trigger_counts[item] = trigger_counts.get(item, 0) + 1

    # Sort foods by frequency and return the top triggers
    sorted_triggers = sorted(trigger_counts.items(), key=lambda x: x[1], reverse=True)
    triggers = [item[0] for item in sorted_triggers if item[1] > 1]  # Only include foods with more than 1 association

    return FoodTriggersResponse(triggers=triggers)

 