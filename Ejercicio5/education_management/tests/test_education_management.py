import pytest
from education_management.education_management import EducationManagement
from education_management.course import Course
from education_management.user import User
from education_management.lesson import Lesson


def test_add_course():
    system = EducationManagement()
    course = Course(1, "Math", "Algebra", "Dr. jose")
    system.manage_courses("add", course)
    assert 1 in system.courses

def test_add_user():
    system = EducationManagement()
    user = User(1, "Daniela", "daniela@gmail.com", "password", "student")
    system.manage_users("add", user)
    assert 1 in system.users

def test_add_user():
    system = EducationManagement()
    user = User(2, "Rick", "rick@gmail.com", "password", "instructor")
    system.manage_users("add", user)
    assert 2 in system.users

def test_add_lesson_to_course():
    course = Course(1, "Math", "Algebra", "Dr. jose")
    lesson = Lesson(1, "Integrate", "Exercises", 3) 

    course.add_lesson(lesson=lesson)

    assert course.lessons[0].lesson_id == 1
    assert course.lessons[0].title == "Integrate"
    assert course.lessons[0].content == "Exercises"
    assert course.lessons[0].duration == 3

def test_updatecontent():
    lesson = Lesson(1, "Integrate", "Exercises", 3) 
    lesson.update_content("Examples")

    assert lesson.content == "Examples"

def test_fail_updatecontent():
    lesson = Lesson(1, "Integrate", "Exercises", 3) 
    with pytest.raises(ValueError) as excinfo:
        lesson.update_content("")

    assert "El contenido no debe estar vacío." in str(excinfo.value)

def test_update_duration():
    lesson = Lesson(1, "Integrate", "Exercises", 3) 
    lesson.update_duration(5)

    assert lesson.duration == 5

def test_fail_update_duration():
    lesson = Lesson(1, "Integrate", "Exercises", 3) 
    with pytest.raises(ValueError) as excinfo:
        lesson.update_duration(-8)

    assert "La duración debe ser un valor positivo." in str(excinfo.value)

def test_add_lesson_to_course():
    lesson = Lesson(1, "Integrate", "Exercises", 3) 

    sum =  lesson.summary()

    assert sum["lesson_id"] == 1
    assert sum["title"] == "Integrate"
    assert sum["content"] == "Exercises"
    assert sum["duration"] == 3
