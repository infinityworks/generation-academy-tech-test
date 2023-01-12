# Generation Academy Tech Test

## The Task

Your team has been given a list of people who work at your company in quoted CSV format, with a requirement to produce a clean output of the CSV file using a Python application _(See below)_.  
Another member of your team has started work on a CSV parser to load the data from this file.  You have been asked to finish the program by implementing the `__parse_row` method in `csvparser.py`.

_Your only area of focus should be the implementation of the method._
  
CSV:
```
"Kacie","Holland","Principal Consultant",""
"Alishia","Burt","Consultant",""
"Yazmin","Rice","Senior Consultant",""
"Edmund","Ramsey","Consultant",""
"Oliver","Rooney","Associate Consultant",""
"Kya","Donaldson","Consultant",""
...
```

Output:
```
Kacie - Holland - Principal Consultant - 
Alishia - Burt - Consultant - 
Yazmin - Rice - Senior Consultant - 
Edmund - Ramsey - Consultant - 
Oliver - Rooney - Associate Consultant - 
Kya - Donaldson - Consultant - 
...
```

There are 3 test files which are all in quoted CSV format - people-list.csv, people-list-comma.csv and people-list-full.csv. The first has no gotchas, the second contains some commas within the data fields, and the last contains escaped quotes - making the task progressively more difficult as it goes on.

_Note_ : Please do not fork the repository.

## Prerequisites

* Python 3
* A clone of this repo
* A suitable dev environment, such as `VSCode`

## Getting Started

Create a new virtual environment:

```sh
# Windows
$ py -m venv venv

# MacOS/Unix
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
# Windows
$ source venv/Scripts/activate

# MacOS/Unix
$ source venv/bin/activate
```

Run the app:

```sh
# Windows
$ py app.py

# MacOS/Unix
$ python3 app.py
```
