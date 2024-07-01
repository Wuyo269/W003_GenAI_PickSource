# ------------------------------------------
# Build in modules
# ------------------------------------------
import os
import json

# ------------------------------------------
# 3rd party modules (installation needed)
# ------------------------------------------
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# ------------------------------------------
# custom modules
# ------------------------------------------
None


def process(data):
    if isinstance(data, dict):
        sorted_data = {k: process(v) for k, v in sorted(data.items())}
        return {k: format_floats(v) for k, v in sorted_data.items()}
    elif isinstance(data, list):
        return [process(item) for item in data]
    else:
        return data


def format_floats(data):
    if isinstance(data, float):
        # Format floats to 10 decimal places as strings
        return f"{data:.10f}"
    else:
        return data


class OpenAILangChainCustom():

    def __init__(self, model_name: str = "gpt-4") -> None:
        # Get api key
        self.apikey = os.getenv("OPENAI_API_KEY")
        if self.apikey == None:
            raise Exception("apikey is empty. Verify environment variable 'OPENAI_API_KEY'.")

        # If model_name is empty use default "gpt-4"
        if model_name != "":
            self.model_name = model_name
        else:
            self.model_name = "gpt-4"
        # Create client
        self.client = ChatOpenAI(
            # Defaults to os.environ.get("OPENAI_API_KEY")
            # Add environment variable "OPENAI_API_KEY"
            model_name=self.model_name
        )
        self.messages = []

    def invoke_question(self, messages: list = None) -> AIMessage:

        if messages == None:
            ai_message = self.client.invoke(self.messages)
        else:
            ai_message = self.client.invoke(messages)
        # return output message
        return ai_message

    def add_message(self, message):
        self.messages.append(message)

    def add_system_message(self, system_message: str):
        self.messages.append(SystemMessage(content=system_message))

    def ask_single_question(self, system_message: str, user_message: str) -> str:
        # Set local messages variable
        messages = []
        # Add SystemMessage to message list
        messages.append(SystemMessage(content=system_message))
        # Add HumanMessage to message list
        messages.append(HumanMessage(content=user_message))
        # invoke with GenAI
        ai_message = self.invoke_question(messages)
        return ai_message.content

    def conversation(self, user_text: str) -> str:
        # Add HumanMessage to message list
        self.add_message(HumanMessage(content=user_text))
        # invoke with GenAI
        ai_message = self.invoke_question()
        # Add AIMessage to message list
        self.add_message(AIMessage(content=ai_message.content))
        return ai_message.content

    def check_moderation(self, moderation_text: str = "I drown kittens.", print_score: bool = False) -> bool:

        # Ask question
        api_response = self.client.moderations.create(input=moderation_text)

        # Moderation result
        moderation_result = api_response.results[0].flagged

        if print_score:
            # Create dictionary from api response
            response_dict = api_response.model_dump()
            # Format dictionary
            formatted_dict = process(response_dict)
            # Print results
            print(json.dumps(formatted_dict, indent=2))
        return moderation_result
