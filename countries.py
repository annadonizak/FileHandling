
def main():
    with open('countries.txt', 'r') as file:
        for i, line in enumerate(file):           ## aut num do kazdej lini 
            print(f'{i+1}. {line}', end="")
    

if __name__ == '__main__':
    main()

    ## main() 