# AI Study Planner

A modern, intelligent study planner built with **FastAPI** and **HTML/CSS/JavaScript** that helps students create personalized study schedules and get AI-powered suggestions.

## Features

- **Smart Schedule Generator**: Input exam date, subjects, and daily hours → instantly get a day-wise study plan
- **Progress Tracking**: Mark days as completed with checkboxes and see real-time progress bar
- **Focus Timer (Pomodoro)**: Built-in 25-minute focus timer with start/pause/reset
- **AI Suggestions**: Get intelligent, personalized study tips using Groq + Llama-3.3-70B
- **Responsive & Clean UI**: Modern glassmorphic design with smooth interactions
- **Fully Functional**: No backend required for frontend (works with FastAPI)

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Templating**: Jinja2
- **AI Integration**: Groq API + Llama-3.3-70B model
- **Styling**: Custom CSS with Font Awesome icons

## How It Works

1. Enter your **Exam Date**, **Subjects** (comma separated), and **Hours per Day**
2. Click **"Generate AI Schedule"**
3. Get a detailed day-wise study schedule
4. Mark completed days using checkboxes to track progress
5. Use the built-in **Focus Timer** for study sessions
6. Read **AI-powered suggestions** for better study habits

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/TauheedSikander/AI-Study-Planner.git
cd AI-Study-Planner

# Install dependencies
pip install fastapi uvicorn jinja2 python-multipart python-dotenv openai

# Run the server
python -m uvicorn main:app --reload

Then open your browser and go to: http://127.0.0.1:8000

```
# Live Demo
(https://ai-study-planner--tauheeddhedhy.replit.app/)

## Project Structure
```bash
AI-Study-Planner/
├── main.py
├── scheduler.py
├── ai_helper.py
├── templates/
│   └── index.html
├── static/
├── .env
├── requirements.txt
└── README.md
```

# Environment Variables
Create a .env file and add:
```bash
GROK_AI_KEY=your_groq_api_key_here
```

# Author
~ Tauheed Sikander
