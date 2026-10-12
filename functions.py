import numpy as np # type: ignore

SUBJECTS = ["Python", "Mathematics", "Statistics", "English"]

def calculate_total(marks):
    """Return the sum of a student's subject marks."""
    return int(np.sum(marks))

def calculate_average(marks):
    """Return the average of a student's subject marks."""
    return round(float(np.mean(marks)), 2)

def assign_grade(average):
    """Assign a grade using the project's grading rules."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

def get_result(marks):
    """A student passes only when every subject mark is at least 40."""
    for mark in marks:
        if mark < 40:
            return "Fail"
    return "Pass"

def attendance_status(attendance):
    """Flag attendance below 75% as low."""
    if attendance >= 75:
        return "Satisfactory"
    return "Low"

def get_top_performers(data, count=3):
    """Return the top students by average marks."""
    return data.sort_values(by="Average", ascending=False).head(count)

def subject_summary(data):
    """Calculate average, highest and lowest mark for each subject."""
    summary = []
    for subject in SUBJECTS:
        summary.append({
            "Subject": subject,
            "Average": round(float(np.mean(data[subject])), 2),
            "Highest": int(np.max(data[subject])),
            "Lowest": int(np.min(data[subject]))
        })
    return summary
