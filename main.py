import re, csv, sys, os

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <logfile or logfolder>")
        exit()

    log_input = sys.argv[1]
    log_entries = list()
    regex_db = list()

    # supports file and directory input
    if os.path.isfile(log_input):
        with open("access.log", 'r') as log_file:
            log_entries = log_file.readlines()
    elif os.path.isdir(log_input):
        log_entries = folder_input(log_input)
    
    # parse the regex database which will be used for matching
    with open('regex.csv') as regex_file:
        csv_reader = csv.reader(regex_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            regex_db.append(row)

    # Loops through each log entry and match it against the regex in the regex database
    for entry in log_entries:
        for regex_query in regex_db:
            match = re.search(regex_query[1], entry)
            if match:
                print('\x1b[0;37;41m' + regex_query[0] + ' detected!' + '\x1b[0m')
                print(entry)

def folder_input(log_input):
    """
        > Process a folder 
        > loop through all files contained within the folder
        > read the file line by line
        > appending to a main list that will be returned back to main
    """
    main_log_entries = list()
    # walking through the directory content
    for root, dirs, files in os.walk(log_input):
        for file in files:
            # gets the full path of the file
            log_file = os.path.join(root, file)
            # open the file for reading
            with open(log_file, 'r') as log_file:
                # read the file line by line and appending to main list
                log_entries = log_file.readlines()
                for entry in log_entries:
                    main_log_entries.append(entry)
    
    return main_log_entries

if __name__ == '__main__':
    main()