###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as f:
    content = f.read()

# write the content to the target file (copy)
with open(target_file, 'w') as f:  #otw copy file
    f.write(content)

    ##Program otwiera plik healthy_lifestyle.txt, odczytuje jego zawartość i zapisuje ją do zmiennej content.
##Następnie otwiera plik copy_healthy_lifestyle.txt (lub tworzy go, jeśli nie istnieje) i zapisuje do niego tę samą zawartość.
##Ostatecznie plik copy_healthy_lifestyle.txt zawiera identyczną zawartość jak healthy_lifestyle.txt.