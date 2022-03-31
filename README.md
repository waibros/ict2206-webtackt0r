# Webtackt0r

:star: A tool created for SIT ICT2206 project - Developing a solution for Web Security. :star:

Web Attack Detector, also known as Webtackt0r, is a post-incident toolkit that assist investigators in identifying web attacks. It does so by performing regular expression matching against log entries, flagging out offending entries and output to a HTML report. 

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