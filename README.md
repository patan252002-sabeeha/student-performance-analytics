# Student Performance Analytics System

## Project overview
A beginner-level Python data-analysis project that reads student records from a CSV file and analyzes marks, grades, pass/fail results, attendance, subject performance and top performers.

## Technologies
- Python
- Pandas
- NumPy
- CSV

## Project files
- `main.py` — runs the analysis and displays results
- `functions.py` — reusable calculation and processing functions
- `students.csv` — sample dataset containing 20 students
- `Project_Documentation.md` — project report and implementation explanation


## Requirements
Python 3.9 or newer is recommended.

Install the libraries:
```bash
python -m pip install pandas numpy
```

## Run the project
Open a terminal in this folder and run:
```bash
python main.py
```

The program prints a student-wise report, class summary, subject-wise performance, top three performers.

## Rules used
- Each student has four subjects, each scored out of 100.
- A student passes only if they score at least 40 in every subject.
- Grade A: average >= 90
- Grade B: average >= 80 and < 90
- Grade C: average >= 70 and < 80
- Grade D: average >= 60 and < 70
- Grade E: average >= 40 and < 60
- Grade F: average < 40
- Attendance below 75% is marked as Low. Attendance does not change the marks-based pass/fail result.


