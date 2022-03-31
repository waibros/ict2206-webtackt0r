# Webtackt0r

:star: A tool created for SIT ICT2206 project - Developing a solution for Web Security. :star:

Web Attack Detector, also known as Webtackt0r, is a post-incident toolkit that assist investigators in identifying web attacks. It does so by performing regular expression matching against log entries, flagging out offending entries and output to a HTML report. 

You may refer to the logs in **sample_logs** folder that were generated for the purpose of studying attack payloads. They are generated from attacking intentionally vulnerable web application such as DVWA and XVWA, and collecting the logs afterwhich. 

A sample output HTML report is included in **sample_reports** for interested reader to know more about the usefulness of the tool. 

Regular expression database (regex.csv) is built from studying of the malicious logs and publicly available payloads such as ones from PayloadAllTheThings and book.hacktricks[.]xyz cheatsheets. 

## Installation
```bash
git clone https://github.com/waibros/ict2206-webtackt0r.git
cd ict2206-webtackt0r/
pip install -r requirements.txt
```

## Requirement
1. Python 3. The tool has been developed and tested with Python 3.10 (latest version as of writing)
2. Jinja2 library

## Usage:
```bash
python3 main.py <log file or folder of log files>
```

## Output:
A HTML report will be generated in the project directory, named YYYY-MM-DDTHHMMSS_report.html e.g. 2022-03-31T172144_report.html. 

## Note:
Do not delete the regex.csv from the project directory as the toolkit relies on the database to function. You may add more regular expressions to the database following the field format "attack_name:attack_query"