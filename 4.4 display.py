filename = 'it_company.csv'


def read_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines() #odczt wiersze z pliku w postaci listy, f zwraca liste
    return lines


def print_lines(lines, start, size=5):
    for line in lines[start:start + size]: #poviera wycinek z listy
        print(line, end="")


def main():
    lines = read_lines(filename) #wczyt wszystkich wierszy w pliku
    total_lines = len(lines) #l wierszy

    key = str() #zmienna przechowuje wartosc jaka dalam
    current_index = 0 #index do drukow

    while (key == '') & (current_index < total_lines): #petla dziala kiedy key jest usty
        print_lines(lines, start=current_index)
        key = input('Press Enter key...')
        current_index += 5 #od ktorego wiesza zaczac druk
    


if __name__ == '__main__':
    main()