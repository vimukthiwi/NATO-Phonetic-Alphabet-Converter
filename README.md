# NATO Phonetic Alphabet Converter

This Python script converts a given word into its NATO phonetic alphabet equivalent.

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```bash
   pip install pandas
   ```

## Usage

1. Ensure you have Python and pandas installed.
2. Run the script:

   ```bash
   python nato_phonetic_converter.py
   ```

3. Follow the prompt to enter a word.
4. The script will output the NATO phonetic alphabet codes corresponding to each letter in the word.

## Example

Suppose you enter the word "HELLO":

```bash
Enter a word: HELLO
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

This shows the NATO phonetic alphabet representation of each letter in the word.

## Files

- `nato_phonetic_converter.py`: The Python script for converting words to NATO phonetic codes.
- `nato_phonetic_alphabet.csv`: CSV file containing the NATO phonetic alphabet data.

## Notes

- The script reads the NATO phonetic alphabet data from `nato_phonetic_alphabet.csv`.
- Ensure the CSV file is present and correctly formatted for proper script execution.
