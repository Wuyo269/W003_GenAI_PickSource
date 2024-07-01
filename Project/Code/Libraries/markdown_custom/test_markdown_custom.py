# ------------------------------------------
# Build in modules
# ------------------------------------------
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


# test load_document
if False:
    file_path =r"C:\Users\mwojcik\Python_Better\W003_GenAI_PickSource\Project\Data\Source\mateusz.md"

    text = load_document(file_path)
    print(text)
    print("Check")

# test append_to_markdown
if True:
    file_path =r"C:\Users\mwojcik\Python_Better\W003_GenAI_PickSource\Project\Data\Source\mateusz.md"

    append_to_markdown(file_path, "Nicpoń jakich mało.")
    print("Check")
