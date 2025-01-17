###
# Saves to a file a list of employees working at a specified position
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r' ) as e: #otw plik z pracownikami 
    with open(position_file, 'w') as p: #otw plik w trybie 'w'
        for line in e. readlines():
            if job_title in line: #czy posiada okreslony tytul
                p.write(line) #zapisuje w pliku jesli jest warun
