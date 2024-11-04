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

def test_add_user():
    system = EducationManagement()
    user = User(1, "Alice", "alice@example.com", "password", "student")
    system.manage_users("add", user)
    assert 1 in system.users

def test_enroll_student_in_course():
    system = EducationManagement()
    course = Course(1, "Math", "Algebra basics", "Dr. Smith")
    user = User(1, "Alice", "alice@example.com", "password", "student")
    system.manage_courses("add", course)
    system.manage_users("add", user)
    course.enroll_student(user.user_id)
    assert user.user_id in course.enrolled_students

def test_add_lesson_to_course():
    course = Course(1, "Math", "Algebra basics", "Dr. Smith")
    lesson = Lesson(1, "Lesson 1", "Introduction to Algebra", 30)
    course.add_lesson(lesson)
    assert len(course.lessons) == 1
    assert course.lessons[0].title == "Lesson 1"