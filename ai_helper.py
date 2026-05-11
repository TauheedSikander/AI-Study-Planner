import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key=os.getenv("GROK_AI_KEY") 

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key= api_key
)

def get_ai_suggestions(schedule):
    try:
        ai_prompt = f"""
           You are an expert study planner.

           Here is a student's study schedule:
           {schedule}

           Suggest improvements to make it more effective. Give clear actionable tips. Keep the answer concise. """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": ai_prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI suggestion failed: {str(e)}"
