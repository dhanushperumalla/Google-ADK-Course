import os
import random
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


load_dotenv()


api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set. Please set it in your .env file.")


model = LiteLlm(
    model="openrouter/openai/gpt-3.5-turbo", 
    api_key=api_key,
)


def get_dad_joke():
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)


root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="Dad joke agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes. 
    Only use the tool `get_dad_joke` to tell jokes.
    """,
    tools=[get_dad_joke],
)