import sys

def num_vowels(text):
    num = 0
    text_lower = text.lower()
    vowels = "aeiou"
    for vowel in text_lower:
        if vowel in vowels:
            num += 1
    return num

def num_whitespaces(text):
    num = 0
    for space in text:
        if space == " ":
            num += 1
    return num

def num_digits(text):
    digits = "0123456789"
    num = 0
    for digit in text:
        if digit in digits:
            num += 1
    return num

def num_words(text):
    string_text = text.split()
    words = len(string_text)
    return words

def inverse(text):
    size = len(text)
    inv = ""
    for ch in range(1, size + 1):
        inv += (text[-ch])
    return inv

def length(text):
    l = len(text)
    return l

def halfs(text):
    half = len(text) / 2
    first_half = text[:int(half)]
    second_half = text[int(half):]
    return first_half, second_half

def upper_vowels(text):
    vowels = "aeiou"
    upper_vowels = ""
    for vowel in text:
        if vowel in vowels:
            upper_vowels += vowel.upper()
        else:
            upper_vowels += vowel
    return upper_vowels

def sorted_by_words(text):
    string_text = text.split()
    stringlist = sorted(string_text)
    sbw = " ".join(stringlist)
    return sbw

def length_of_words(text):
    string_text = text.split()
    list1 = list()
    listsize = len(string_text)
    for i in range(listsize):
        value = len(string_text[i])
        list1.append(str(value))
    low = " ".join(list1)
    return low

text = sys.argv[1]
print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of numbers: ", num_digits(text))
print("Number of words: ", num_words(text))
print("Inverse of text: ", inverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", halfs(text))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
