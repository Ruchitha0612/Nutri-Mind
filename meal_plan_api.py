from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Dict

router = APIRouter()

class MealPlanRequest(BaseModel):
    user_id: str
    allergies: List[str] = Field(default_factory=list)
    dietary_restrictions: List[str] = Field(default_factory=list)
    recent_symptoms: List[str] = Field(default_factory=list)

class MealDetail(BaseModel):
    meal: str
    explanation: str

class DayPlan(BaseModel):
    breakfast: MealDetail
    lunch: MealDetail
    dinner: MealDetail

class MealPlanResponse(BaseModel):
    days: List[DayPlan]

@router.post("/meal-plan", response_model=MealPlanResponse)
async def generate_meal_plan(request: MealPlanRequest):
    # Simple, hardcoded gut-friendly meal plan
    plan = [
        DayPlan(
            breakfast=MealDetail(
                meal="Oatmeal with blueberries",
                explanation="Oatmeal is gentle on the gut and blueberries are low-FODMAP."
            ),
            lunch=MealDetail(
                meal="Grilled chicken with rice and steamed carrots",
                explanation="Chicken and rice are easy to digest; carrots are gut-friendly."
            ),
            dinner=MealDetail(
                meal="Baked salmon with quinoa and zucchini",
                explanation="Salmon provides healthy fats; quinoa and zucchini are mild and nutritious."
            ),
        ),
        DayPlan(
            breakfast=MealDetail(
                meal="Rice cakes with peanut butter and banana",
                explanation="Rice cakes are gluten-free; peanut butter and banana are generally well-tolerated."
            ),
            lunch=MealDetail(
                meal="Turkey and spinach salad with olive oil",
                explanation="Turkey is lean; spinach and olive oil support gut health."
            ),
            dinner=MealDetail(
                meal="Stir-fried tofu with bok choy and jasmine rice",
                explanation="Tofu is a good protein source; bok choy and rice are gentle on digestion."
            ),
        ),
        DayPlan(
            breakfast=MealDetail(
                meal="Scrambled eggs with sautéed spinach",
                explanation="Eggs and spinach are mild and nutritious."
            ),
            lunch=MealDetail(
                meal="Quinoa bowl with grilled shrimp and cucumber",
                explanation="Quinoa and cucumber are easy on the gut; shrimp is a light protein."
            ),
            dinner=MealDetail(
                meal="Chicken soup with carrots and potatoes",
                explanation="Chicken soup is classic for gut comfort; carrots and potatoes are low-FODMAP."
            ),
        ),
    ]
    return MealPlanResponse(days=plan) 