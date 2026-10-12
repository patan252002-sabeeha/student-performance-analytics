# Project Documentation: Student Performance Analytics System

## 1. Introduction
The Student Performance Analytics System is a simple Python project that processes student records and produces useful academic summaries. It demonstrates core Python concepts and basic data analysis using Pandas and NumPy.

## 2. Problem statement
Reviewing marks for many students manually takes time and can lead to calculation errors. This project automates common calculations and presents student-wise and class-wise results in a readable format.

## 3. Objectives
- Read student records from a CSV file.
- Organize records in a Pandas DataFrame.
- Calculate total and average marks.
- Assign grades and pass/fail status.
- Analyze class and subject performance.
- Identify the top three performers.

## 4. Tools and libraries
- **Python:** program logic, conditions, loops, and functions.
- **Pandas:** CSV reading, DataFrame operations, sorting, grouping, and output.
- **NumPy:** numerical calculations such as sum, mean, minimum, and maximum.
- **CSV:** stores the original student dataset.

## 5. Dataset description
The supplied `students.csv` contains 20 fictional students. Fields include:
- `Student_ID`: unique student identifier
- `Name`: student name
- `Department`: academic department
- `Python`, `Mathematics`, `Statistics`, `English`: subject marks out of 100
- `Attendance`: attendance percentage

## 6. Rules and assumptions
### Grade rule
| Average marks | Grade |
|---|---|
| 90 and above | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| 40 to below 60 | E |
| Below 40 | F |

### Pass/fail rule
A student passes only if every subject mark is at least 40. If any subject mark is below 40, the student fails. Attendance is reported separately; attendance below 75% is labelled Low and does not alter the marks-based result.

## 7. Implementation
1. `pd.read_csv()` loads the CSV into a DataFrame.
2. `head()`, `info()`, and `len()` show the data preview, structure, and record count.
3. A loop visits each row and collects subject marks.
4. Functions calculate totals, averages, grades, pass/fail status, and attendance status.
5. NumPy calculates numerical summaries.
6. Pandas sorting identifies the top three students.
7. Subject-wise summaries are calculated.


## 8. Expected outputs
When `main.py` runs, it displays:
- Dataset preview and basic information
- Total and average marks for each student
- Grade, pass/fail result, and attendance status
- Class average, highest and lowest student average
- Number of passed and failed students and pass percentage
- Subject-wise average, highest and lowest marks
- Best and lowest-performing subjects by average
- Top three performers


Exact values are calculated from the included CSV dataset when the program runs.

## 9. Testing checklist
- [ ] Run the program with the supplied CSV.
- [ ] Confirm 20 student records load.
- [ ] Check that totals equal the sum of four subject marks.
- [ ] Check that averages equal total divided by four.
- [ ] Verify that any student with a subject mark below 40 is marked Fail.
- [ ] Verify grade boundaries using averages of 40, 60, 70, 80, and 90.
- [ ] Confirm top performers are sorted from highest to lowest average.


## 10. Conclusion
This project demonstrates how Python, NumPy, and Pandas can be used to automate simple student-performance reporting. It applies variables, data types, loops, conditions, functions, and data-analysis operations.


