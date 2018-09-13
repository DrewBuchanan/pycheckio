import string

def checkio(text: str) -> str:
    text = text.lower()
    chars = {}
    for char in text:
        if not char.isalpha():
            continue
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    sorted_chars = sorted(chars.items(), key=lambda kv: kv[1], reverse = True)
    first = sorted_chars[0]
    for x in sorted_chars:
        if x[1] >= first[1] and string.ascii_lowercase.index(first[0]) > string.ascii_lowercase.index(x[0]):
            first = x

    return first[0]


def tests():
    print(checkio("Hello World!"))
    print(checkio("How do you do?"))
    print(checkio("One"))
    print(checkio("Oops!"))
    print(checkio("AAaooo!!!!"))
    print(checkio("abe"))
    print(checkio("a" * 9000 + "b" * 1000))

tests()