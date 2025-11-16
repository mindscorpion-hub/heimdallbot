import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

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
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    model_name = 'gemini-2.0-flash-001'
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    try:
        response = client.models.generate_content(
            model = model_name, 
            contents = messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )
    except Exception as e:
        print("Generate error:", repr(e))
        sys.exit(1)

    # python
    calls = []
    cands = getattr(response, "candidates", []) or []
    for c in cands:
        content = getattr(c, "content", None)
        parts = getattr(content, "parts", []) if content else []
        for p in parts:
            fc = getattr(p, "function_call", None)
            if fc:
                calls.append(fc)

    if calls:
        for fc in calls:
            print(f"Calling function: {fc.name}({fc.args})")
    else:
        print(response.text)
    #print(f"User prompt: {prompt}")
    #print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
