from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter()

# MongoDB setup
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["nutri_mind"]
meal_plan_collection = db["meal_plans"]

class MealPlan(BaseModel):
    user_id: str
    plan: Dict[str, Any]  # Flexible structure for meal plan details

@router.post("/set-meal-plan", response_model=MealPlan)
async def set_meal_plan(meal_plan: MealPlan):
    existing = await meal_plan_collection.find_one({"user_id": meal_plan.user_id})
    if existing:
        await meal_plan_collection.replace_one({"user_id": meal_plan.user_id}, meal_plan.dict())
    else:
        await meal_plan_collection.insert_one(meal_plan.dict())
    return meal_plan

@router.get("/get-meal-plan/{user_id}", response_model=MealPlan)
async def get_meal_plan(user_id: str):
    meal_plan = await meal_plan_collection.find_one({"user_id": user_id})
    if not meal_plan:
        raise HTTPException(status_code=404, detail="Meal plan not found for this user.")
    meal_plan.pop("_id", None)
    return meal_plan 