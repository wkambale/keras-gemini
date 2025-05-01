from keras_gemini import KerasGemini
import google.generativeai as genai

# Initialize Gemini and the KerasGeminiPlugin
genai.configure(api_key="YOUR_API_KEY") # Replace with your actual API key
keras_plugin = KerasGemini()
model = genai.GenerativeModel(model_name='gemini-pro')

# Interactive loop for user input
print("Welcome to the Keras-Gemini Model Builder!")
print("Type a prompt like 'Build a 3-layer sequential model', or 'exit' to quit.")

while True:
    prompt = input("\nEnter a prompt: ")    
    if prompt.lower() == "exit":        
        print("Exiting...")
        break
    response = model.generate_content(prompt)
    print(response.text)
    response = model.generate_content(prompt)
    print(response)

    if keras_plugin.model:
        keras_plugin.model.summary()
