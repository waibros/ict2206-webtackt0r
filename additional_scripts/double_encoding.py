from curses.ascii import isalpha
import urllib.parse
'''
This script is to double-encode SQL keywords and format into regular expression form. 
'''
keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'COLLATE', 'CASE', 'SUBSTR', 'SUBSTRING', 'NULL', 'ORDER BY', 'UNION', 'UNION ALL', 'FROM dual']
final_text = ''
for keyword in keywords:
    temp = ''
    for character in keyword:
        if isalpha(character) or character == '_' or character == '.':
            temp += "%" + format(ord(character), "x")
        else:
            temp += urllib.parse.quote(character, safe='')
    final_text += urllib.parse.quote(temp, safe='').upper() + "|"

print(final_text)