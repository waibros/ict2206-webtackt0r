from curses.ascii import isalpha
import urllib.parse
'''
This script is to double-encode SQL keywords and format into regular expression form. 
'''
keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'COLLATE', 'CASE', 'SUBSTR', 'SUBSTRING', 'NULL', 'ORDER BY', 'UNION', 'UNION ALL', 'FROM dual']
single_encoded = double_encoded = unicode_encoded = charunicodeescape = ''
for keyword in keywords:
    temp = ''
    for character in keyword:
        if isalpha(character) or character == '_' or character == '.':
            temp += "%" + format(ord(character), "x")
        else:
            temp += urllib.parse.quote(character, safe='')

    single_encoded += temp.upper() + "|"
    double_encoded += urllib.parse.quote(temp, safe='').upper() + "|"
    unicode_encoded += temp.upper().replace("%", "%u00") + "|"
    charunicodeescape += temp.upper().replace("%", "%5Cu00") + "|"

print("Single encoded regex: \n" + single_encoded)
print("\nDouble encoded regex: \n" + double_encoded)
print("\nUnicode encoded regex: \n" + unicode_encoded)
print("\nCharunicodeescape tamper script regex: \n" + charunicodeescape)