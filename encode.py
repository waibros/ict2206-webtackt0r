import urllib.parse, sys, os

if len(sys.argv) != 2:
    print("Usage: python3/python encode.py <logfile>")
    exit()

log_input = sys.argv[1]

if os.path.isfile(log_input):
    with open(log_input, 'r') as source:
        with open("out"+log_input, 'w') as output:
            for i, line in enumerate(source):
                if i > 0:
                    output.write("(" + urllib.parse.quote_plus(line) + ")|")
                output.write("(" + urllib.parse.quote_plus(line) + ")")
    print("Successfully parsed to URL Encoded REGEX Format at out" + log_input)
else:
    print("Not a file.")
    exit()



