from curses.ascii import isalpha
import urllib.parse
import string
'''
This script is to generate character-encoded strings and format into regular expression form. 
'''
def tamper_overlongutf8more(keyword_list):
    """
        Reference: 
            * https://github.com/sqlmapproject/sqlmap/blob/master/tamper/overlongutf8more.py
    """
    encoded_string = ''
    for keyword in keyword_list:
        temp = keyword
        if keyword:
            temp = ""
            i = 0
            while i < len(keyword):
                if keyword[i] == '%' and (i < len(keyword) - 2) and keyword[i + 1:i + 2] in string.hexdigits and keyword[i + 2:i + 3] in string.hexdigits:
                    temp += keyword[i:i + 3]
                    i += 3
                else:
                    temp += "%%%.2X%%%.2X" % (0xc0 + (ord(keyword[i]) >> 6), 0x80 + (ord(keyword[i]) & 0x3f))
                    i += 1

        encoded_string += temp + '|'
    return encoded_string

# List of keywords to catch
keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'COLLATE', 'CASE', 'SUBSTR', 'SUBSTRING', 'NULL', 'ORDER BY', 'UNION', 'UNION ALL', 'FROM dual']
single_encoded = double_encoded = unicode_encoded = charunicodeescape = ''
overlongutf8_encoded = tamper_overlongutf8more(keywords)
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
print("\nOverlong UTF8 encoded tamper script regex: \n" + overlongutf8_encoded)