filename = 'it_company.csv'


def read_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def print_lines(lines, start, size=5):
    for line in lines[start:start + size]:
        print(line, end="")


def main():
    lines = read_lines(filename)
    total_lines = len(lines)

    key = str()
    current_index = 0

    while (key == '') & (current_index < total_lines):
        print_lines(lines, start=current_index)
        key = input('Press Enter key...')
        current_index += 5


if __name__ == '__main__':
    main()