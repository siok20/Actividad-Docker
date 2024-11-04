import pytest
from education_management.education_management.education_management import EducationManagement
from education_management.education_management.course import Course
from education_management.education_management.lesson import Lesson
from education_management.education_management.user import User

def test_add_course():
    system = EducationManagement()
    course = Course(1, "Math", "Algebra", "Dr. jose")
    system.manage_courses("add", course)
    assert 1 in system.courses
