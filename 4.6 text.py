def analyze_file():
    try:
        filename = input("Enter the filename: ")

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        num_lines = len(lines)

        num_characters = sum(len(line) for line in lines)

        num_words = sum(len(line.split()) for line in lines)

        print(f"File name: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")

    except FileNotFoundError:
        print("The file does not exist. Please check the filename and try again.")


def main():
    analyze_file()
    

if __name__ == '__main__':
    main()