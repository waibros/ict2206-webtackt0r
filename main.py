import re, csv, sys, os
from jinja2 import Template
import time

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <logfile or logfolder>")
        exit()

    log_input = sys.argv[1]
    log_entries = list()
    regex_db = list()

    # supports file and directory input
    if os.path.isfile(log_input):
        with open(log_input, 'r') as log_file:
            log_entries = log_file.readlines()
    elif os.path.isdir(log_input):
        log_entries = folder_input(log_input)
    
    # parse the regex database which will be used for matching
    with open('regex.csv') as regex_file:
        csv_reader = csv.reader(regex_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            regex_db.append(row)

    # Format: log_entry = [triggered rule #1, triggered rule #2 ... triggered rule #3]
    offending_entry_dict = {}
    
    for entry in log_entries:
        for regex_query in regex_db:
            match = re.search(regex_query[1], entry, re.IGNORECASE)
            if match:
                # check if the log_entry is in the dictionary or not, otherewise creates the key and the new list of triggered rule
                # else, append new triggered rule to the list. 
                if entry in offending_entry_dict:
                    offending_entry_dict[entry].append(regex_query[0])
                else:
                    offending_entry_dict[entry] = [regex_query[0]]
    
    date_time = time.strftime("%Y-%m-%dT%H%M%S")
    # Uncomment this for final submission
    html_report(offending_entry_dict, date_time)

    # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal 
    for key, valuelist in offending_entry_dict.items():
        print('\x1b[0;30;43m' + 'Offending entry:' +'\x1b[0m')
        print('{}'.format(key))
        print('\x1b[0;30;43m' + 'Rule(s) triggered:' +'\x1b[0m')
        for value in valuelist:
            print(value)
        print('-'*100)

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

def html_report(dict_input, date_time):
    html_string = '''
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <title>Hello, world!</title>
    </head>
    <body>
        <br>
        <br>
        <h1 class="display-1 text-center">Webtackt0r Web Attacks report</h1>
        <br>
        <br>
        <h3>Report generated on {{ date_time }}</h3>
        <br>
        <div class="table-responsive">
            <table class="table table-dark table-striped table-bordered" style="max-width: none; table-layout: fixed; word-wrap: break-word;">
                <thead>
                    <tr>
                        <th scope="col">Rule Triggered</th>
                        <th scope="col">Log Entry</th>
                    </tr>
                </thead>
                <tbody>
                    {% for key,valuelist in entries_dict.items() %}
                        <tr> 
                            <td>
                                {% for value in valuelist %}
                                    <li>{{ value }}</li>
                                    <br>
                                {% endfor %}
                            </td>        
                            <td>
                                <p>
                                    {{ key }}
                                </p>
                            </td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    </body>
    </html>
    '''

    j2_template = Template(html_string)
    filename = date_time + '_report.html'
    f = open(filename,'w')
    f.write(j2_template.render(entries_dict=dict_input, date_time=date_time))
    f.close()

if __name__ == '__main__':
    main()