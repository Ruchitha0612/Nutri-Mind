from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel, Field
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
import os
import openai

router = APIRouter()

# MongoDB setup
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["nutri_mind"]
collection = db["user_profiles"]

# Pydantic model
class UserProfile(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    food_allergies: List[str] = Field(default_factory=list)
    dietary_restrictions: List[str] = Field(default_factory=list)
    health_goals: List[str] = Field(default_factory=list)

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key in environment

@router.post("/user/profile", response_model=UserProfile)
async def set_user_profile(profile: UserProfile):
    existing = await collection.find_one({"user_id": profile.user_id})
    if existing:
        await collection.replace_one({"user_id": profile.user_id}, profile.dict())
    else:
        await collection.insert_one(profile.dict())
    return profile

@router.get("/user/profile/{user_id}", response_model=UserProfile)
async def get_user_profile(user_id: str):
    profile = await collection.find_one({"user_id": user_id})
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found.")
    # Remove MongoDB's _id field for Pydantic validation
    profile.pop("_id", None)
    return profile

class ChatRequest(BaseModel):
    user_message: str

@router.post("/chat")
async def chat_with_gpt(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": (
                    "You are a helpful nutrition and gut health assistant. "
                    "Answer user questions about gut health, and explain the reasoning behind AI-generated nutrition plans in a clear, supportive way."
                )},
                {"role": "user", "content": request.user_message}
            ],
            max_tokens=400,
            temperature=0.7,
        )
        answer = response.choices[0].message["content"].strip()
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def generate_meal_suggestion(symptom_logs: list, food_logs: list, restrictions: list = []) -> str:
    # Calls OpenAI or other LLM, returns a meal suggestion string
    ... 