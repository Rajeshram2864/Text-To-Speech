# Text Feature Extraction with NLTK

This project demonstrates a basic approach to natural language processing (NLP) focusing on text tokenization, frequency distribution, and boolean feature extraction using NLTK (Natural Language Toolkit). It provides a fundamental building block for text classification or sentiment analysis tasks.

## Features
- **Text Tokenization**: Breaks down raw text messages into individual words (tokens).
- **Frequency Distribution (Bag-of-Words)**: Calculates the frequency of each word across a collection of messages.
- **Boolean Feature Extraction**: Generates a dictionary of boolean features, indicating the presence or absence of predefined "important" words in a given message.

## Installation
To run this code, you need to have Python and the NLTK library installed.

1.  **Install Python**:
    If you don't have Python installed, download it from the [official Python website](https://www.python.org/downloads/).

2.  **Install NLTK**:
    Open your terminal or command prompt and run the following command:
    ```bash
    pip install nltk
    ```

3.  **Download NLTK Data (punkt tokenizer)**:
    NLTK requires certain datasets to perform its operations. For `word_tokenize`, you'll need the `punkt` tokenizer. Open a Python interpreter and run:
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage
The code processes a collection of messages (`processed`), creates a frequency distribution of all words, and then defines a function to extract boolean features from a single message.

**Prerequisites**:
- You need a variable named `processed` which should be an iterable (e.g., a list) of strings, where each string is a text message.
- You need to define `word_features`, which is a list of words you consider "important" for feature extraction. This is typically derived from the most frequent words in your `all_words` frequency distribution.

```python
from nltk.tokenize import word_tokenize
import nltk # Ensure nltk is imported for FreqDist

# --- 1. Prepare your raw text data ---
# Example 'processed' data (replace with your actual data)
processed = [
    "This is a great movie, I loved it!",
    "The plot was terrible, I hated it.",
    "It was an okay film, not great but not bad either.",
    "I love good movies and this one was truly great."
]

# --- 2. Tokenize all words and build a frequency distribution ---
all_words = []
for message in processed:
    # Convert message to lowercase to treat "The" and "the" as the same word
    words = word_tokenize(message.lower())
    for w in words:
        all_words.append(w)

# Create a frequency distribution of all words
all_words_freq_dist = nltk.FreqDist(all_words)

# --- 3. Define 'word_features' (e.g., the 2000 most common words) ---
# This is a critical step not fully shown in the original snippet.
# 'word_features' is a list of words you want to check for presence/absence.
# A common approach is to take the N most common words from your corpus.
num_features = 2000 # You can adjust this number
word_features = [word for word, frequency in all_words_freq_dist.most_common(num_features)]

# --- 4. Define the feature extraction function ---
def find_features(message):
    message_words = word_tokenize(message.lower()) # Tokenize and lowercase the message
    features = {}
    for word in word_features:
        features[word] = (word in message_words) # Check if word is present
    return features

# --- 5. Example usage: Extract features for the first message ---
print("--- Features for the first message: ---")
features_first_message = find_features(processed[0])

# Print only the features that are marked as True (present in the message)
present_words = [key for key, value in features_first_message.items() if value is True]
print(f"Original message: '{processed[0]}'\nWords present from word_features: {present_words}")

print("\n--- Example for the second message: ---")
features_second_message = find_features(processed[1])
present_words_second_message = [key for key, value in features_second_message.items() if value is True]
print(f"Original message: '{processed[1]}'\nWords present from word_features: {present_words_second_message}")

# You can now use the 'features_first_message' dictionary for machine learning models.
# e.g., (features_first_message, "positive") or (features_second_message, "negative")
```

## API Reference

### `find_features(message: str) -> dict`

This function takes a single text message and returns a dictionary of boolean features.

**Parameters**:
- `message` (`str`): The text message for which to extract features.

**Returns**:
- `dict`: A dictionary where keys are words from the globally defined `word_features` list, and values are `True` if the word is present in the input `message`, `False` otherwise.

**Dependencies**:
- `nltk.tokenize.word_tokenize`: Used internally to tokenize the input `message`.
- `word_features`: A global list of words that are used as features. This list **must be defined** before calling `find_features`.

## Architecture
The architecture is simple and sequential:

1.  **Data Collection**: An external `processed` list of text messages serves as the initial input.
2.  **Global Word Tokenization**: All words from all messages in `processed` are tokenized and collected into a single list (`all_words`).
3.  **Frequency Distribution**: `nltk.FreqDist` is used to create a frequency map of all collected words. This step implicitly forms the basis for defining "important" words.
4.  **Feature Set Definition (`word_features`)**: A global list `word_features` is created, typically containing the most common words from the frequency distribution. This forms the vocabulary for feature extraction.
5.  **Feature Extraction Function (`find_features`)**: This function acts as the core logic for transforming a single message into a boolean feature vector based on `word_features`.
6.  **Application**: The `find_features` function is called for specific messages, and the resulting boolean feature dictionaries can be used for further NLP tasks.

```
+----------------+       +-------------------+       +---------------------+
|    'processed' |------>|                   |------>|  all_words_freq_dist|
| (List of Texts)|       |  Tokenize & Collect |       | (nltk.FreqDist object)|
+----------------+       |    All Words      |       +---------------------+
                         | (Populates all_words) |               |
                         +-------------------+               | (most common words)
                                                             v
                                                     +---------------------+
                                                     |    'word_features'  |
                                                     | (List of select words)|
                                                     +---------------------+
                                                                ^
                                                                |
                                             +------------------+-------------------+
                                             |                                     |
                                             |  Input 'message' (string)           |
                                             |                                     |
                                             v                                     v
                                    +---------------------+                    +----------------------+
                                    |    word_tokenize    |                    |                      |
                                    | (Tokenize message)  |                    |   find_features(message) |
                                    +---------------------+                    | (Checks for word presence)|
                                             |                                 +----------------------+
                                             v                                            |
                                    +---------------------+                               v
                                    |  Message Words      |                     +---------------------+
                                    | (List of tokens)    |<--------------------|  Output 'features'  |
                                    +---------------------+                     |   (Dict of Booleans)|
                                                                                +---------------------+
```

## Contributing
Contributions are welcome! If you find a bug, have a suggestion for improvement, or want to add a new feature, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature-name`
3.  **Make your changes.**
4.  **Commit your changes** with a clear and descriptive message: `git commit -m "feat: Add new feature X"` or `git commit -m "fix: Resolve bug Y"`
5.  **Push your branch** to your forked repository: `git push origin feature-name`
6.  **Open a Pull Request** to the `main` branch of this repository.

Please ensure your code adheres to good practices and includes appropriate documentation and tests if applicable.

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code, provided you include the original license.
