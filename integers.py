def calculate_and_save_powers():
    with open("powers.txt", "w") as file:
        for i in range(1, 101):
            square = i ** 2
            cube = i ** 3

            result = f"{i},{square},{cube}"
            print(result)
            file.write(result + "\n")  #file.write(result + "\n"): Zapisuje wynik do pliku powers.txt, dodając znak nowej linii po każdym wpisie.


def main():
    calculate_and_save_powers()


if __name__ == '__main__':
    main()




    ## unkcja calculate_and_save_powers:
##Oblicza kwadrat i sześcian liczb od 1 do 100.
##Zapisuje wyniki do pliku w formacie CSV (przecinki jako separatory).
##Wyświetla wyniki w konsoli.

##worzenie pliku tekstowego powers.txt z tabelą potęg liczb od 1 do 100






