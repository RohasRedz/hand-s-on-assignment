def capitalize_vowels(s):
    new_str = ""
    vowels = "aeiou"
    for i in s:
        if i in vowels:
            new_str += i.upper()
        else:
            new_str += i
    return new_str


if __name__ == "__main__":
    print(capitalize_vowels("Apoorv Chaudhary"))
