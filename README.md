# Generation Academy Tech Test

## The Task

Your team has been given a list of people who work at your company in quoted CSV format, with a requirement to produce a clean output of the CSV file using a Python application _(See below)_.
Another member of your team has started work on a CSV parser to load the data from this file.  You have been asked to finish the program by implementing the `__parse_row` method in `csvparser.py`.

_Your only area of focus should be the implementation of the method._

CSV:

```text
"Kacie","Holland","Principal Consultant",""
"Alishia","Burt","Consultant",""
"Yazmin","Rice","Senior Consultant",""
"Edmund","Ramsey","Consultant",""
"Oliver","Rooney","Associate Consultant",""
"Kya","Donaldson","Consultant",""
...
```

Output:

```text
Kacie - Holland - Principal Consultant -
Alishia - Burt - Consultant -
Yazmin - Rice - Senior Consultant -
Edmund - Ramsey - Consultant -
Oliver - Rooney - Associate Consultant -
Kya - Donaldson - Consultant -
...
```

_Note_ : Please do not fork the repository.

## Sample data

Three example .csvs have been included in the `data` directory. Solve the problem for `people-list.csv` first, then if time consider updating the code to ensure edge cases in `people-list-comma.csv`, and then `people-list-full.csv` are also handled.

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
