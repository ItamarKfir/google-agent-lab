import asyncio
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk import Message  # <-- 1. Import the Message class

def get_weather(city: str) -> dict:
    """Returns fake weather for a city."""
    return {
        "city": city,
        "weather": "sunny",
        "temperature": "26C",
    }

root_agent = Agent(
    name="basic_ai_engineer_agent",
    model="gemini-2.5-flash",
    description="A basic AI engineering learning agent.",
    instruction=(
        "You are a helpful AI engineering tutor. "
        "Explain GCP, agents, APIs, REST APIs, Pub/Sub, Cloud Run, and Vertex AI simply."
    ),
    tools=[get_weather],
)

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name="WeatherTutorApp")
    
    print("Sending prompt to agent...")
    async for event in runner.run_async(
        user_id="local_dev_user",
        session_id="session_01",
        # 2. Wrap your string in a Message object and specify the "user" role
        new_message=Message(role="user", content="Hi! Can you tell me the weather in Tokyo?")
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, 'text') and part.text:
                    print(part.text, end="")
    print()

if __name__ == "__main__":
    asyncio.run(main())