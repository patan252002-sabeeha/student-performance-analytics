import pandas as pd # type: ignore
import numpy as np # type: ignore
from functions import (
    SUBJECTS,
    calculate_total,
    calculate_average,
    assign_grade,
    get_result,
    attendance_status,
    get_top_performers,
    subject_summary,
)

def main():
    # Step 1: Read the CSV file into a Pandas DataFrame.
    data = pd.read_csv("students.csv")

    print("=" * 68)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 68)

    # Step 2: Inspect the dataset.
    print("\n =========== STUDENT DATA ==========")
    print(data.head().to_string(index=False))
    print(f"\nNumber of students: {len(data)}")
    print(f"Number of columns: {len(data.columns)}")
    

    # Step 4: Use a loop to calculate each student's totals and average.
    totals = []
    averages = []
    results = []
    grades = []
    attendance = []

    for _, student in data.iterrows():
        marks = [student[subject] for subject in SUBJECTS]
        total = calculate_total(marks)
        average = calculate_average(marks)
        totals.append(total)
        averages.append(average)
        results.append(get_result(marks))
        grades.append(assign_grade(average))
        attendance.append(attendance_status(student["Attendance"]))

    data["Total"] = totals
    data["Average"] = averages
    data["Grade"] = grades
    data["Result"] = results
    data["Attendance_Status"] = attendance

    # Step 5: Display each student's analysis.
    print("\nSTUDENT-WISE PERFORMANCE")
    columns_to_show = ["Student_ID", "Name", "Department", "Total", "Average",
                       "Grade", "Result", "Attendance", "Attendance_Status"]
    print(data[columns_to_show].to_string(index=False))

    # Step 6: Class performance statistics using NumPy/Pandas.
    print("\nCLASS SUMMARY")
    print(f"Overall class average: {np.mean(data['Average']):.2f}")
    print(f"Highest student average: {data['Average'].max():.2f}")
    print(f"Lowest student average: {data['Average'].min():.2f}")
    print(f"Students passed: {(data['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(data['Result'] == 'Fail').sum()}")
    print(f"Pass percentage: {(data['Result'].eq('Pass').mean() * 100):.2f}%")
    print(f"Average attendance: {np.mean(data['Attendance']):.2f}%")

    # Step 7: Subject-wise analysis.
    print("\nSUBJECT-WISE PERFORMANCE")
    subject_data = pd.DataFrame(subject_summary(data))
    print(subject_data.to_string(index=False))
    best_subject = subject_data.loc[subject_data["Average"].idxmax(), "Subject"]
    weakest_subject = subject_data.loc[subject_data["Average"].idxmin(), "Subject"]
    print(f"Best-performing subject by average: {best_subject}")
    print(f"Lowest-performing subject by average: {weakest_subject}")

    # Step 8: Top three students.
    print("\nTOP 3 PERFORMERS")
    top_students = get_top_performers(data, 3)
    print(top_students[["Student_ID", "Name", "Department", "Average", "Grade"]].to_string(index=False))



if __name__ == "__main__":
    main()
