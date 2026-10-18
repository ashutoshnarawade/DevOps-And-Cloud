import pytest
from app.routes.api import app
from app.services import academic_service as service


@pytest.fixture(autouse=True)
def reset_data():
    service.students.clear()
    service.courses.clear()
    service.enrollments.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_create_student(client):
    response = client.post(
        "/students",
        json={"student_id": "S1", "name": "Rahul"}
    )
    assert response.status_code == 201


def test_enrollment_credit_limit():
    service.add_student("S1", "Rahul")
    service.add_course("C1", "Programming", 10)
    service.add_course("C2", "Mathematics", 9)

    service.enroll_student("S1", "C1", "Semester1")
    with pytest.raises(ValueError, match="18 credits"):
        service.enroll_student("S1", "C2", "Semester1")


def test_duplicate_enrollment():
    service.add_student("S1", "Rahul")
    service.add_course("C1", "Programming", 3)
    service.enroll_student("S1", "C1", "Semester1")

    with pytest.raises(ValueError, match="already enrolled"):
        service.enroll_student("S1", "C1", "Semester1")


def test_gpa_calculation():
    service.add_student("S1", "Rahul")
    service.add_course("C1", "Programming", 3)
    service.add_course("C2", "Mathematics", 3)
    service.enroll_student("S1", "C1", "Semester1")
    service.enroll_student("S1", "C2", "Semester1")
    service.assign_grade("S1", "C1", "Semester1", "A")
    service.assign_grade("S1", "C2", "Semester1", "B")

    assert service.calculate_gpa("S1", "Semester1") == 9.0
