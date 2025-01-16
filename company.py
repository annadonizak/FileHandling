###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'


def read_employees(file_name):
    count = 1           #count jest licznikiem, który nadaje numerację
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if job_title in line:
                print(f'{count}. {line}', end="")
                count += 1       #count jest zwiększany o 1 po każdej iteracji, gdy znajdzie wiersz zawierający Software Engineer.


def main():
    read_employees(file_name)


if __name__ == '__main__':
    main()