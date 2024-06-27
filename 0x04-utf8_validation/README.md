# 0x04-utf8_validation

## Description
Project intended to learn about UTF-8 encoding and how to validate if a 
given data set is a valid UTF-8 encoding.

### What is UTF-8?
UTF-8 is a variable-width character encoding capable of encoding all 
1,112,064 valid code points in Unicode using one to four one-byte (8-bit) 
code units. The encoding is defined by the Unicode Standard, and was originally
designed by Ken Thompson and Rob Pike. The name is derived from Unicode 
(or Universal Coded Character Set) Transformation Format – 8-bit.

### How to validate UTF-8 encoding?
A character in UTF-8 can be 1 to 4 bytes long. The bytes are 8 bits long,
and are subject to the following rules:
- A 1-byte character begins with a 0.
- A n-byte character begins with n 1's followed by a 0.
- A n-byte character uses n-1 bits for the code, and the remaining bit is
a continuation bit.
- The following are valid UTF-8 encodings:
  - 0xxxxxxx
  - 110xxxxx 10xxxxxx
  - 1110xxxx 10xxxxxx 10xxxxxx
  - 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

