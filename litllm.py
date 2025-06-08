#litellm 

# Import required classes and functions from the agents package
from agents import Agent, Runner, set_tracing_disabled

# Import the model for interacting with Gemini via LiteLLM
from agents.extensions.models.litellm_model import LitellmModel

# Import dotenv to load environment variables from the .env file
from dotenv import load_dotenv

# Import os to access environment variables
import os

# Load environment variables from .env file
load_dotenv()

# Disable tracing (optional – useful for keeping the logs clean)
set_tracing_disabled(disabled=True)

# Get the Gemini API key from the environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Create a new agent named "assistant" with specific instructions
my_agent = Agent(
    name="assistant",
    
    # Instructions to the AI agent about how to respond when someone says hi or hello
    instructions="when someone say hi or hello You have to answer say Assalam o alikum I'm a muslim agent how can i help you?",
    
    # Define the model the agent will use (Gemini model via LiteLLM)
    model=LitellmModel(
        model="gemini/gemini-2.0-flash",
        api_key=api_key
    )
)

# Ask the user for input
user = input("Write something... ")

# Use Runner to run the agent synchronously with the user's input
respond = Runner.run_sync(
    my_agent, user
)

# Print the final response from the agent
print(respond.final_output)
