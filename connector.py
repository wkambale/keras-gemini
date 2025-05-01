import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "i need high level programming to build a python package that combines the power of keras and gemini. the idea is to incoporate the steps and structure of keras in building neural networks into gemini where a user simply has to write normal language as a prompt like \"Build a 3-layer sequential network/model\" and the prompt will be executed as tho i have written the actual keras code. add all necessary dependencies and considerations to make this work efficiently.",
      ],
    }
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)