# Encoding-scripts

## 1. Atbash Cipher

The Atbash cipher is a substitution cipher that has a specific key where each letter is flipped to it’s opposite value: A to Z becomes Z to A.  For efficiency sake, we are going be working with ASCII values. For the sake of simplicity, I will only be allowing alphabetic values.  All numbers and special characters will be stripped from the initial string.


#### Steps of the encryption and decryption algorithm:
- Remove all characters except letters and convert the string to lowercase
- Depending on the operation, encode or decode the message
- Encoding or decoding consists in setting elements by index from an inverted alphabet
- In case of incorrect operation selection, inform the user about the error
- Output the finished result
