from keras_gemini import KerasGemini
import google.generativeai as genai

# Initialize Gemini and the KerasGeminiPlugin
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel(model_name='gemini-pro')
keras_plugin = KerasGemini(model)

# Example: Attempt to build a convolutional model (unsupported)
prompt = "Build a 4-layer convolutional network"
response = model.generate_content(prompt)  

print(response)  # Should indicate the model type is unsupported

# The model should remain None
assert keras_plugin.model is None, "Model should not be created for an unsupported type."