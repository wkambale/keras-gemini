import google.generativeai as genai
import os
from keras_gemini import KerasGemini  # Assuming this is the class for interacting with the API

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model and the KerasGeminiPlugin
model = genai.GenerativeModel('gemini-pro')
keras_plugin = KerasGemini(model)

# Example: Build a basic 3-layer sequential model
prompt = "Build a 3-layer sequential model"
response = keras_plugin.generate_content(prompt)

print(response)  # Should indicate the model was built successfully

# Display the model summary
if keras_plugin.model:
    keras_plugin.model.summary()
