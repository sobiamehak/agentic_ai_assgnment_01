
#-----------------------------------------------------------------------------#

# using open router

# Import required modules and classes
from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Disable tracing (useful for debugging or disabling logs)
set_tracing_disabled(disabled=True)

# Get API key from environment variables
api_key = os.getenv("ROUTING_API_KEY")

# Create an agent with instructions for answering English-related questions
english_agent = Agent(
    name="English_teacher",
    instructions="Your job is to answer questions about the English language, including grammar, verbs, modal verbs, vocabulary, words with Urdu meanings, sentence formation, and paragraph writing."
)

# Initialize OpenAI client with API key and base URL for OpenRouter
openai_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Create a wrapper model using DeepSeek Qwen3-8B via OpenAI chat completion model
wrapped_model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    openai_client=openai_client
)

#Configure the model and provider for the Runner
run_config = RunConfig(
    model=wrapped_model,
    model_provider=openai_client,
)

# Take input from user
user_question = input("Ask me anything about the English language: ")

# Run the agent with the given input and configuration
result = Runner.run_sync(english_agent, user_question, run_config=run_config)

# Print the final output from the agent
print(result.final_output)



