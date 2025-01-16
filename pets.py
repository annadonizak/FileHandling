def read_pets(file='pets.txt'):      #def f read_pets main daje read_pets
    with open(file, 'r') as f:    # 'r' form odczyt
        content = f.read()

    print(content)

    words = content.split()
    print('\n Word count:', len(words))


def main():
    read_pets()


if __name__ == '__main__':
    main()