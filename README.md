# Vigenère Cipher Solver

This project is a simple Python implementation to solve a Vigenère cipher given a ciphertext and a suspected key length. The program analyzes the frequency of letters within chunks of the ciphertext (based on the provided key length) and applies a shift to decrypt the message.

## Features

- **Ciphertext Input**: The user can input any ciphertext that needs to be decrypted.
- **Key Length Input**: The user specifies the suspected length of the Vigenère cipher key.
- **Letter Frequency Analysis**: The program counts letter frequencies to estimate the most likely key used in the cipher.
- **Decryption**: The program applies the calculated shifts to each chunk of the ciphertext to decrypt it.

## How It Works

1. The ciphertext is divided into chunks based on the suspected key length.
2. For each chunk, the program calculates the frequency of each letter and determines the most frequent letter.
3. Based on the most frequent letter, the program estimates the shift used for encryption.
4. The program then applies the shift to decrypt each letter and reconstruct the original message.

## Prerequisites

- Python 3.x

## How to Use

1. Clone or download the repository to your local machine.
2. Run the `app.py` script using Python.

```bash
python app.py
```

3. The program will prompt you for two inputs:
   - **Ciphertext**: The encrypted message.
   - **Key Length**: The suspected length of the encryption key.

4. The program will output the decrypted message.

## Example

```bash
Enter the cipher text: UVSORQYSVR
Enter the suspected key length: 3
Decrypted message: HELLOWORLD
```

## Limitations

- The accuracy of decryption depends heavily on the correct estimation of the key length.
- The program assumes that the ciphertext contains uppercase letters only and does not handle non-alphabetic characters.

## Contributing

Feel free to fork this repository, submit issues, or send pull requests if you'd like to contribute or improve the code.

## License

This project is licensed under the MIT License.



