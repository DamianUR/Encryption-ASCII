# ASCII Base Encryption & Decryption

A Python script that encrypts and decrypts text messages by converting characters to ASCII values and representing them in a user-specified numeric base.

---

## Description

This program prompts the user to choose an action (encrypt or decrypt), a numeric base (2–36), and a message. For encryption, each character is converted to its ASCII code and then represented in the chosen base. Decryption reverses the process — converting the base-encoded numbers back to ASCII codes and then to their original characters.

---

## Requirements

- Python 3.x

---

## How to Run

```bash
python encryptAndDecrypt.py
```

The program will prompt you interactively:

1. **Action** — either `encrypt` or `decrypt`
2. **Base** — an integer between 2 and 36
3. **Message** — the text to encrypt, or the encoded string to decrypt

---

## Example Usage

### Encryption
```
Do you want to encrypt or decrypt? Enter below:
encrypt
Enter base of process (2-36): 16
Enter the message below:
Hello
```
**Output:** `48 65 6C 6C 6F`

### Decryption
```
Do you want to encrypt or decrypt? Enter below:
decrypt
Enter base of process (2-36): 16
Enter the message below:
48 65 6C 6C 6F
```
**Output:** `Hello`

---

## Functions Overview

| Function | Description |
|----------|-------------|
| `encrypt(base, msg_str)` | Encrypts a message string into base-encoded ASCII numbers |
| `decrypt(base, num_str)` | Decrypts a base-encoded string back to the original message |
| `conv_to_ascii_string(s)` | Converts a string to a space-separated sequence of ASCII values |
| `conv_to_base(in_num, N)` | Converts an integer to a specified base (up to base 36) |
| `conv_to_decimal(num_str, N)` | Converts a base-N number string back to decimal |
| `conv_arr_base(arr, N)` | Converts each element of an array to a specified base |
| `conv_arr_to_dec(arr, base)` | Converts each base-N element of an array to decimal |
| `scan_num_str(num_str)` | Splits a space-separated number string into an array |
| `base10_arr_to_string(arr)` | Converts an array of ASCII codes to a character string |
| `to_string(arr)` | Joins array elements into a single space-separated string |

---

## Supported Bases

Any base from **2** (binary) to **36** (uses digits `0–9` and letters `A–Z`).

---

## Author

Udorilwela Ratshikhopha
