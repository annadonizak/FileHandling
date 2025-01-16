import re


def count_vowels():
    text = input("Enter your text: ")

    vowel_pattern = r'[aeiouAEIOU]'

    vowels = re.findall(vowel_pattern, text)
    num_vowels = len(vowels)

    print(f"Number of vowels in the text: {num_vowels}")


def main():
    count_vowels()


if __name__ == '__main__':
    main()