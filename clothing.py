import csv

FILENAME = 'clothing.csv'


def read_clothing(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            price = float(row['Price'])
            stock = int(row['Stock_Quantity'])
            if (price < 60) and (stock < 40):
                print(row)


def main():
    read_clothing(FILENAME)


if __name__ == '__main__':
    main()
