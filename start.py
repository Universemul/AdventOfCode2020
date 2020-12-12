import getopt
import sys
import os
import requests
import datetime
import shutil

URL = "https://adventofcode.com/{year}/day/{day}/input"
PWD = os.getcwd()
COOKIE_SESSION=os.getenv("AOC_SESSION") # See https://github.com/wimglenn/advent-of-code-data/tree/ed7cd3ff807228d5e78abbde02276231182ce986
TEMPLATE=f"{PWD}/templates/main.py"
TEMPLATE_PERF=f"{PWD}/templates/perf.py"


def current_day():
    now = datetime.datetime.now()
    day = min(now.day, 25)
    return day

def current_year():
    now = datetime.datetime.now()
    return now.year

def create_context(url: str, day_number: int):
    r = requests.get(url, cookies={"session": COOKIE_SESSION})
    directory = f"{PWD}/day{day_number}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/input.txt", 'wb') as f:
        f.write(r.content)
    if os.path.exists(TEMPLATE): #Copy template in directory
        shutil.copyfile(TEMPLATE, f"{directory}/main.py") 
    if os.path.exists(TEMPLATE_PERF): #Copy template in directory
        shutil.copyfile(TEMPLATE_PERF, f"{directory}/perf.py") 


def usage():
    print('start.py {day number}')
    exit(1)

def main():
    day = current_day()
    year = current_year()
    create_context(URL.format(day=day, year=year), day)


def usage():
    print('start.py {day number}')
    exit(1)

def main():
    day = current_day()
    year = current_year()
    create_context(URL.format(day=day, year=year), day)

if __name__ == "__main__":
    main()
