from typing import Union
import google.generativeai as genai 
from keras import layers, models

class KerasGemini():
    def __init__(self, ):
        
        self.model = None

    def on_init(self):
        print("Keras plugin initialized.")

    def post(self, prompt: str, response: str) -> str:
        model = genai.GenerativeModel(model_name="gemini-pro")
        if prompt.startswith("Build a"):
            # Extract model specifications from prompt using regular expressions
            match = re.search(
                r"Build a (?P<layers>\d+)-layer (?P<type>\w+) model", prompt
            )
            if match:
               num_layers = int(match.group("layers"))
                model_type = match.group("type")

                # Build the Keras model based on extracted information
                self.model = self.build_model(num_layers, model_type)
                if self.model:
                    response += "\nModel built successfully."
                else:
                    response += "\nError building the model. Please check your prompt."
        return response

    def build_model(self, num_layers: int, model_type: str) -> Union[models.Sequential, None]:
        """
        Builds a Keras sequential model based on user prompt.

        Args:
            num_layers: Number of layers in the model.
            model_type: Type of model (e.g., 'sequential').

        Returns:
            A compiled Keras Sequential model or None if model type is invalid.
        """
        if model_type.lower() == "sequential":
            model = models.Sequential()
            # Add layers (assuming Dense layers for simplicity)
            for i in range(num_layers):
                model.add(layers.Dense(128, activation="relu"))  # Example layer
            # Add output layer
            model.add(layers.Dense(10, activation="softmax"))  # Example output layer
            model.compile(
                optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
            )
            return model
        else:
            print(f"Unsupported model type: {model_type}")
            return None
