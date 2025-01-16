def filter_files_with_four_char_extensions():
    try:
        with open("files.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            name, extension = line.rsplit('.', 1)
            if len(extension) == 4:
                print(line)

    except FileNotFoundError:
        print("The file 'files.txt' does not exist. Please check the filename and try again.")

def main():
    filter_files_with_four_char_extensions()


if __name__ == '__main__':
    main()