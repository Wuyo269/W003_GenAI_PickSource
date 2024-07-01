### Prerequisites
Create account on https://platform.openai.com/api-keys. <br>
Save OpenAI API KEY in Environment Variables as "OPENAI_API_KEY"


### Description
The program is an interactive conversation with GenAI. <br>
This program allows you to either pose a question or input new information about an individual to GenAI. <br>
It comprises three source files, each corresponding to a specific individual. <br>
GenAI determines if the user's input is a question or if it's new information that needs to be added to the source file. <br>
If the source file is not recognized, the user will be notified.<br>
When a user poses a question, the program loads data from the relevant source file into the prompt context and generates an answer based on that data. <br>
If a user inputs new information, the program add this information into the corresponding source file.<br>

