from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define prompt template
template = """
Answer the below question.
Here is the conversation history: {history}
Question: {question}
Answer:
"""

# Load the model
model = OllamaLLM(model="llama3")

# Create a chain from the prompt and model
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Chat handler
def handle_conversation():
    history = ""
    print("Welcome to the AI Chatbot !! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # ✅ Use the chain (NOT model), and keys must match template
        result = chain.invoke({"history": history, "question": user_input})
        
        print("Bot:", result)
        history += f"\nUser: {user_input}\nBot: {result}"

if __name__ == "__main__":
    handle_conversation()
