##który zapisuje dane zawierające tytuł filmu, jego reżysera i głównego aktora do pliku tekstowego
# Program to write movie details to a text file

# Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Name of the file to write to
file_name = 'movie_details.txt'

# Writing movie details to the file
with open(file_name, 'w') as file:   #open(file_name, 'w'): Otwiera plik w trybie zapisu (write mod
   file.write(f"Movie Title: {movie_title}\n")
   file.write(f"Director: {director}\n")         #f-strings: Używane do osadzenia zmiennych ({movie_title}, {director}, {lead_actor}) w ciągu tekstowym.
   file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")