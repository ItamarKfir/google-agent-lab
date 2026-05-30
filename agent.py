from google.adk.agents import Agent


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
    instruction="You are a helpful AI engineering tutor.",
    tools=[get_weather],
)