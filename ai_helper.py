import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROK_AI_KEY")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

def get_ai_suggestions(schedule):
    try:
        ai_prompt = f"""
You are a helpful and encouraging study coach.

Here is the student's current study schedule:
{schedule}

Give **clear, actionable, and positive** suggestions to improve this schedule.

Rules:
- Use simple, friendly language.
- Use bullet points only (- or •).
- Do not use markdown like ** or numbers like 1., 2.
- Do not repeat or show the original schedule/dictionary.
- Do not include code or examples of the dictionary.
- Keep it concise (5 to 8 bullet points maximum).
- Focus on: time management, breaks, revision, weak subjects, motivation, etc.

Write the response in clean, readable plain text.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": ai_prompt}],
            temperature=0.65,
            max_tokens=700
        )

        text = response.choices[0].message.content.strip()

        # Clean unwanted markdown and artifacts
        text = text.replace("**", "").replace("```", "").replace("1.", "-").replace("2.", "-").replace("3.", "-")
        text = text.replace("Example:", "").strip()

        return text

    except Exception as e:
        return f"AI suggestion failed: {str(e)}"