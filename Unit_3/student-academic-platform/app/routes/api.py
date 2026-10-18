from flask import Flask, jsonify, request
from app.services import academic_service as service

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "message": "Student Academic Management Platform",
        "status": "running"
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.post("/students")
def create_student():
    data = request.get_json(silent=True) or {}
    student_id = data.get("student_id")
    name = data.get("name")

    if not student_id or not name:
        return jsonify({"error": "student_id and name are required"}), 400

    if student_id in service.students:
        return jsonify({"error": "Student already exists"}), 409

    return jsonify(service.add_student(student_id, name)), 201


@app.post("/courses")
def create_course():
    data = request.get_json(silent=True) or {}

    try:
        course = service.add_course(
            data["course_id"],
            data["name"],
            int(data["credits"])
        )
        return jsonify(course), 201
    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


@app.post("/enrollments")
def create_enrollment():
    data = request.get_json(silent=True) or {}

    try:
        enrollment = service.enroll_student(
            data["student_id"],
            data["course_id"],
            data["semester"]
        )
        return jsonify(enrollment), 201
    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


@app.post("/grades")
def create_grade():
    data = request.get_json(silent=True) or {}
    grade = data.get("grade")

    if grade not in {"A", "B", "C", "D", "F"}:
        return jsonify({"error": "Grade must be A, B, C, D or F"}), 400

    try:
        enrollment = service.assign_grade(
            data["student_id"],
            data["course_id"],
            data["semester"],
            grade
        )
        return jsonify(enrollment), 200
    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


@app.get("/students/<student_id>/gpa/<semester>")
def get_gpa(student_id, semester):
    return jsonify({
        "student_id": student_id,
        "semester": semester,
        "gpa": service.calculate_gpa(student_id, semester)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
