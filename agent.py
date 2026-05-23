import asyncio
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner  # This handles the complex contexts

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
    # Pass your agent to the runner and give your local app a name
    runner = InMemoryRunner(agent=root_agent, app_name="WeatherTutorApp")
    
    # Run the session asynchronously. The runner will handle generating the context!
    print("Sending prompt to agent...")
    async for event in runner.run_async(
        user_id="local_dev_user",
        session_id="session_01",
        new_message="Hi! Can you tell me the weather in Tokyo?"
    ):
        # ADK emits a stream of event objects. Let's capture the text.
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, 'text') and part.text:
                    print(part.text, end="")
    print() # New line after stream ends

if __name__ == "__main__":
    asyncio.run(main())