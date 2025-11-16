import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

def main():
#    print("Hello from heimdallbot!")    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) == 1:
        print('Please input a prompt: uv run main.py <"your prompt here">')
        sys.exit(1)
    
    if len(sys.argv) >= 2:
        prompt = sys.argv[1]
        
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    model_name = 'gemini-2.0-flash-001'
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,            
        ]
    )
    response = client.models.generate_content(
    model = model_name, 
    contents = messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
)

    #if len(sys.argv) >= 3:
    if response.function_calls != None:
        for item in response.function_calls:
            print(f"Calling function: {item.name}({item.args})")
    else:
        print(response.text) 
    #print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
