# ------------------------------------------
# Build in modules
# ------------------------------------------
import os.path

None
# ------------------------------------------
# 3rd party modules (installation needed)
# ------------------------------------------
from langchain.document_loaders.text import TextLoader

# ------------------------------------------
# custom modules
# ------------------------------------------
None


def load_document(file_path: str) -> str:
    # Load markdown document
    loader = TextLoader(file_path, encoding="utf-8")
    # Read content of Markdown document
    doc = loader.load()[0]
    # Get page content
    text = doc.page_content
    return text


def append_to_markdown(file_path: str, new_information: str):
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write('\n' + new_information)
