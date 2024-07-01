# ------------------------------------------
# Build in modules
# ------------------------------------------
import os.path

# ------------------------------------------
# 3rd party modules (installation needed)
# ------------------------------------------
None

# ------------------------------------------
# custom modules
# ------------------------------------------
from Project.Code.Libraries.open_ai_lang_chain_custom import open_ai_lang_chain_custom
from Project.Code.Libraries.markdown_custom import markdown_custom
from Project.Code.Libraries.framework.framework import FrameWork

# OpenAI model
open_ai_model = "gpt-4"

# Sources - files names
sources = [
    {"name": "Ania (Nunek)", "source": "ania.md"},
    {"name": "Pawel (Ojciec)", "source": "pawel.md"},
    {"name": "Mateusz (Wuyo)", "source": "mateusz.md"}
]

# Format sources in text format
sources_text_formatted = '\n'.join([f"{source['name']} file: {source['source']}" for source in sources])

# Calc prompts full paths
prompt_1_pick_source_path = os.path.join(FrameWork.PROMPT_FOLDER_PATH, "prompt_1_pick_source_file")
prompt_2_question_or_task_path = os.path.join(FrameWork.PROMPT_FOLDER_PATH, "prompt_2_question_or_task")
prompt_3_answer_question_path = os.path.join(FrameWork.PROMPT_FOLDER_PATH, "prompt_3_answer_question")

# Load prompts
with open(prompt_1_pick_source_path) as file:
    prompt_1_pick_source_file = file.read()

with open(prompt_2_question_or_task_path) as file:
    prompt_2_question_or_task = file.read()

with open(prompt_3_answer_question_path) as file:
    prompt_3_answer_question = file.read()

# Add sources to Prompt 1
prompt_1_pick_source_file = prompt_1_pick_source_file.replace("sources_text_formatted_placeholder",
                                                              sources_text_formatted)

# Create instance of custom OpenAI class
open_ai_instance = open_ai_lang_chain_custom.OpenAILangChainCustom(open_ai_model)

while True:
    # Get user query
    user_query = input("User:")
    # If user writes Exit - end the loop
    if user_query.lower() == "exit":
        break

    # Get the source file based on the user query
    response = open_ai_instance.ask_single_question(prompt_1_pick_source_file, user_query)

    # If None user query is not related to current sources files.
    if response.lower() == "None".lower():
        print("AI: I do not have a source for this person.")
    else:
        print(f"Source found: {response}")
        # Calc source full path
        source_path = os.path.join(FrameWork.SOURCE_FOLDER_PATH, response)
        # Decide if user wants to ask a question or add information to file
        question_or_task = open_ai_instance.ask_single_question(prompt_2_question_or_task, user_query)

        if question_or_task.lower() == "None".lower():
            print(f"Unable to define if this is a question or task.")
        else:
            print(f"This is a {question_or_task}")
            if question_or_task.lower() == "question".lower():
                # Load data from source file
                context = markdown_custom.load_document(source_path)
                # Add data to prompt context
                prompt_3_answer_question_copy = prompt_3_answer_question.replace("context_placeholder",
                                                                                 context)
                # Respond on user query based on source data.
                response = open_ai_instance.ask_single_question(prompt_3_answer_question_copy, user_query)
                if response.lower() == "None".lower():
                    print("I do not know that.")
                else:
                    print(response)
            else:
                markdown_custom.append_to_markdown(source_path, user_query)
                print(f"Information added to source file '{response}'")
