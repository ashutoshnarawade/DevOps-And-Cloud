students = {}
courses = {}
enrollments = []


def add_student(student_id, name):
    students[student_id] = {"name": name}
    return students[student_id]


def add_course(course_id, name, credits):
    if credits <= 0:
        raise ValueError("Course credits must be positive")
    courses[course_id] = {"name": name, "credits": credits}
    return courses[course_id]


def enroll_student(student_id, course_id, semester):
    if student_id not in students:
        raise ValueError("Student not found")
    if course_id not in courses:
        raise ValueError("Course not found")

    existing = [
        e for e in enrollments
        if e["student_id"] == student_id
        and e["semester"] == semester
    ]

    if any(e["course_id"] == course_id for e in existing):
        raise ValueError("Student is already enrolled in this course")

    total_credits = sum(courses[e["course_id"]]["credits"] for e in existing)
    if total_credits + courses[course_id]["credits"] > 18:
        raise ValueError("Maximum 18 credits allowed per semester")

    enrollment = {
        "student_id": student_id,
        "course_id": course_id,
        "semester": semester,
        "grade": None
    }
    enrollments.append(enrollment)
    return enrollment


def assign_grade(student_id, course_id, semester, grade):
    for enrollment in enrollments:
        if (
            enrollment["student_id"] == student_id
            and enrollment["course_id"] == course_id
            and enrollment["semester"] == semester
        ):
            enrollment["grade"] = grade
            return enrollment
    raise ValueError("Enrollment not found")


def calculate_gpa(student_id, semester):
    records = [
        e for e in enrollments
        if e["student_id"] == student_id
        and e["semester"] == semester
        and e["grade"] is not None
    ]
    credits = sum(courses[e["course_id"]]["credits"] for e in records)
    if credits == 0:
        return 0.0
    points = {"A": 10, "B": 8, "C": 6, "D": 4, "F": 0}
    weighted_points = sum(
        points[e["grade"]] * courses[e["course_id"]]["credits"]
        for e in records
    )
    return round(weighted_points / credits, 2)
