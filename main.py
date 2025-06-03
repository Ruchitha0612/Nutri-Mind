from fastapi import FastAPI
from user_profile_api import router as user_profile_router
from get_food_triggers import router as food_triggers_router
from weekly_summary_api import router as weekly_summary_router
# ... import other routers as needed

app = FastAPI()

app.include_router(user_profile_router)
app.include_router(food_triggers_router)
app.include_router(weekly_summary_router)
# ... include other routers as needed

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to Nutri Mind API!"} 