# Python Autocorrect

Welcome to Python Autocorrect! This project is designed to provide autocorrection functionality for text inputs using Python.

## Overview

Python Autocorrect leverages text processing techniques to suggest corrections for misspelled words. It utilizes a corpus of words from a text file and calculates the similarity between the input word and the words in the vocabulary to offer the most probable corrections.

## How it Works

1. **Data Preparation**: The project reads a text file containing a corpus of words and processes it to create a vocabulary.

2. **Word Frequency Calculation**: It calculates the frequency of each word in the vocabulary.

3. **Probability Calculation**: Probabilities for each word are calculated based on their frequency in the corpus.

4. **Autocorrection**: When provided with a misspelled word, the project suggests corrections by finding similar words from the vocabulary and ranking them based on their similarity and probability.

## Getting Started

To use Python Autocorrect, follow these steps:

1. **Install Dependencies**: Make sure you have the required dependencies installed. You can install them using `pip`:
   ```
   pip install pandas textdistance
   ```

2. **Run the Code**: Execute the Python script to load the text file, process the data, and define the autocorrection function.

3. **Use the Autocorrection Function**: Call the `my_autocorrect` function with a misspelled word as input to receive suggestions for corrections.

## Example

```python
from autocorrect import my_autocorrect

# Example usage
print(my_autocorrect("howeve"))
```

## Contribution

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to contribute to this project. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
