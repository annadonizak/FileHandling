###
# Calculates the total value of money spent
#
import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding='utf8') as f:   #with open(email_file, 'r', encoding='utf8') as f: Otwiera plik report.txt w trybie do odczytu ('r'). Używa również kodowania 'utf8', aby poprawnie obsługiwać różne znaki (np. polskie litery).
    email = f.read()

# regular expression pattern
# for amounts
pattern = '€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total_amount = 0
for amount in amounts:
    total_amount += int(amount)

# print result
print(f'Total spendings: €{total_amount}')