import base64
import codecs

"""
    Get the flag from text
    Flag format: Py4SE{FLAG}
    Process to get this text:
    Base64 -> ROT13 -> Decimal -> Hex -> Binary -> Base 64
"""
# decoding a Base64 string
text = 'MDEwMDEwMDAgMDEwMTAxMDEgMDExMTEwMDAgMDAxMTAwMDAgMDEwMDEwMDAgMDAxMTAwMDAgMDEwMDEwMDEgMDAxMTAxMTEgMDEwMDExMDAgMDExMTAxMTEgMDEwMDAxMDEgMDExMDExMDEgMDEwMTEwMTAgMDAxMTAwMDEgMDAxMTEwMDEgMDExMTAxMTEgMDEwMTEwMTAgMDEwMTAxMDAgMDAxMTAxMDEgMDAxMTAwMTAgMDEwMTEwMTAgMDAxMTAwMTEgMDEwMTAxMTEgMDAxMTAwMDAgMDEwMTEwMTAgMDAxMTAwMTEgMDEwMTAxMTEgMDExMTAwMTEgMDEwMTEwMTAgMDExMTAxMTEgMDEwMDExMDAgMDAxMTAwMDEgMDEwMTEwMTAgMDExMTAxMTEgMDEwMTAxMTEgMDAxMTEwMDE='
text_bytes = text.encode()
text_bytes = base64.b64decode(text_bytes)
text = text_bytes.decode()

text = text.split()

chars = []

for i in text:
    # convert bin to dec
    # then, convert dec to char
    chars.append(chr(int(i, 2)))
# convert list to string
chars= "".join(chars)
# decode rot13
text = codecs.encode(chars, 'rot_13')
# decoding a Base64 string
text_bytes = text.encode()
text_bytes = base64.b64decode(text_bytes)
text = text_bytes.decode()
# get the flag
flag = text[6 : -1]

print("Flag: " + flag)
