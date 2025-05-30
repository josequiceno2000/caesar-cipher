alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]

def caesar(text: str, shift: int, encode_or_decode: str) -> str:
    if encode_or_decode == "decode":
        shift *= -1
    return "".join([alphabet[(alphabet.index(char) + shift) % 26] if char in alphabet else char for char in text])