# keras-gemini

[![Release](https://img.shields.io/pypi/v/keras-gemini?label=Release&style=flat-square)](https://pypi.org/project/keras-gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package that combines the power of Keras with Gemini for natural language-driven neural network building.

### Built With

- Python
- Keras
- Gemini API
- NLTK

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.x

### Installation

```sh
pip install keras-gemini
```

## Usage

```python
from keras_gemini import prompt_to_keras

model = prompt_to_keras("Build a 3-layer sequential model")
if model:
    model.summary()
```

## Run the Examples
To run these examples, users simply need to navigate to the examples/ directory and run any of the scripts. For example:

```bash
python examples/build_basic_model.py
```

## Features
- Natural Language Model Building: Build Keras sequential models by simply describing the desired architecture in natural language.

For example: `Build a 3-layer sequential model`

- Automatic Model Compilation: The package automatically compiles the generated Keras model with default settings: 

- `optimizer='adam'`
- `loss='sparse_categorical_crossentropy'`
- `metrics=['accuracy']`

- Seamless Integration with Gemini: The `KerasGemini()` integrates directly into your Gemini chatbot flow, allowing for natural conversational model building.

## Upcoming Features (Roadmap)
- [ ] Support for More Layer Types: Add support for a wider range of Keras layers (Convolutional, Recurrent, etc.) to enable building diverse network architectures.

- [ ] Customizable Layer Parameters: Allow users to specify layer parameters (activation functions, number of units, etc.) through natural language prompts.

- [ ] Advanced NLP for Model Understanding: Implement more robust natural language processing techniques to better extract user intent and complex model specifications.

- [ ] Model Training and Evaluation: Provide functionality to train and evaluate the generated Keras models directly within the Gemini conversation.

- [ ] Model Persistence: Allow users to save and load their custom-built models for later use.

- [ ] Interactive Model Building: Enable users to iteratively refine their models by adding or removing layers, modifying parameters, and getting feedback in real-time.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [License](https://github.com/wkambale/keras_gemini/blob/main/LICENSE) for more information.