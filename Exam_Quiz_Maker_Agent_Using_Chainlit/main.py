import os
from dotenv import load_dotenv
import google.generativeai as genai
import chainlit as cl


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key = gemini_api_key)


model = genai.GenerativeModel(
    model_name = "gemini-2.0-flash"
)


@cl.on_chat_start
async def greeting():
    await cl.Message(
        content = (
            "📝 Welcome to the Quiz Generator Agent!\n\n"
            "Just tell me the topic — like `JavaScript`, `AI`, or `Science` — and I’ll generate quiz questions with answers for you. 🎯\n"
            "Let’s make learning fun!"
            )
            ).send()



@cl.on_message
async def chat(message : cl.Message):
    prompt = f"Create a quiz of unlimited questions with answer.{message.content}"
    res = model.generate_content(prompt)
    await cl.Message(content = res.text).send()