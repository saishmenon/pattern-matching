# Importing Regular expression operations module
import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

inputText = input("Enter a text or sentence: ")

mo = phoneNumberRegex.search(inputText)
print('The Phone number found is: ' + mo.group())