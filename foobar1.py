def answer(s):
    CYPHER_DICT = {"a": "z", "b": "y", "c": "x", "d": "w",
                   "e": "v", "f": "u", "g": "t", "h": "s", "i": "r",
                   "j": "q", "k": "p", "l": "o", "m": "n", "n": "m",
                   "o": "l", "p": "k", "q": "j", "r": "i", "s": "h",
                   "t": "g", "u": "f", "v": "e", "w": "d", "x": "c",
                   "y": "b", "z": "a"}

    encrypted_str = s
    decrypted_str = ""

    for c in encrypted_str:
        if c.islower():
            decrypted_str += CYPHER_DICT[c]
        else:
            decrypted_str += c

    return decrypted_str
