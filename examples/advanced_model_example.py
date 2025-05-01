from keras_gemini import KerasGemini
import google.generativeai as genai

# Initialize Gemini and the KerasGeminiPlugin
genai.configure(api_key="YOUR API KEY")
model = genai.GenerativeModel('gemini-pro')
keras_plugin = KerasGemini(model)
# Example: Build a  sequential model with more natural language and a training process
prompt = "build a sequential model with 5 layers and train it"
response = model.generate_content(prompt)
print("response from the model")
print(response)  # Should indicate the model was built successfully

# Display the model summary
if keras_plugin.model:
    keras_plugin.model.summary()
