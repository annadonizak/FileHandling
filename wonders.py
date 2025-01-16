###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders_sorted = sorted(seven_wonders)      #sorted() zwraca nową listę zawierającą elementy z listy seven_wonders, ale posortowaną alfabetycznie.

# Write data to the file
with open(file_name, 'w') as f:
  for item in seven_wonders_sorted:
     f.write(item + '\n')