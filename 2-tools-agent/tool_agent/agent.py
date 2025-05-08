from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def current_time() -> dict:
    """You are a tool that can return the current date and time."""

    return {"current_time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name = 'tool_agent',
    model='gemini-2.0-flash',
    instruction="""You are a helpful assistant that can use the following tools:
    
    - current_Time
    """,
    description="Tool Agent",
    # tools=[google_search]
    tools=[current_time,]

)