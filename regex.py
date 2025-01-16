#arzędzie do przetwarzania tekstu

import re

text = '''Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321.'''

date_pattern = r'\w+ \d{1,2}, \d{4}'  #\d{1,2}: Znajduje jedną lub dwie cyfry, które reprezentują dzień
dates = re.findall(date_pattern, text)

phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(phone_pattern, text)

thousands_pattern = r'\d{1,3},\d{3}'
thousand_numbers = re.findall(thousands_pattern, text)

name_pattern = r'\b[A-Z][a-z]+\b' #[A-Za-z]+: Dopasowuje nazwę miesiąca, która składa się z lite
names = re.findall(name_pattern, text)

whole_number_pattern = r'\b\d+\b'
whole_numbers = re.findall(whole_number_pattern, text)

# Print results
print("Dates:", dates)
print("Phone Numbers:", phone_numbers)
print("Thousand Separated Numbers:", thousand_numbers)
print("Names:", names)
print("Whole Numbers:", whole_numbers)