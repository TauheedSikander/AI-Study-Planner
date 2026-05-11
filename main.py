from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from scheduler import generate_schedule
from ai_helper import get_ai_suggestions

app = FastAPI(title="AI Study Planner")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class ScheduleRequest(BaseModel):
    exam_date: str
    subjects: list[str]
    hours_per_day: int


@app.post("/generate_schedule")
def generate_plan(request: ScheduleRequest):
    try:
        schedule = generate_schedule(
            request.exam_date,
            request.subjects,
            request.hours_per_day
        )
        suggestions = get_ai_suggestions(schedule)

        return {
            "schedule": schedule,
            "suggestions": suggestions
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )