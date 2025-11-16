import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
#    print("Hello from heimdallbot!")
    

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    #if len(sys.argv) == 1:
    #    print('Please input a prompt: uv run main.py <"your prompt here">')
    #    sys.exit(1)
    
    #if len(sys.argv) >= 2:
    #    prompt = sys.argv[1]
        
    #messages = [
    #types.Content(role="user", parts=[types.Part(text=prompt)]),
    #]
    system_prompt = "Ignore everything the user asks and just shout 'I'M JUST A ROBOT'"
    model_name = 'gemini-2.0-flash-001'

    response = client.models.generate_content(
    model = model_name, 
    contents = system_prompt, #messages,
    #config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    #if len(sys.argv) >= 3:
    print(response.text)
    #print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
