from fastapi import APIRouter
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.models.courses_model import CoursesModel
from app.models.db_session import create_session, global_init
from app.schemas import Course, CourseCreate, CourseEdit, CourseSave

global_init("./database/kairos.db")
db_ses = create_session()
kairos = APIRouter(tags=["General Endpoints"])


@kairos.post("/gen")
def generate_course(course: CourseCreate):
    return {"hello": "world"}


@kairos.post("/save")
def save_course_to_database(course: CourseSave):
    try:
        course_to_save = CoursesModel.from_pydantic(course=course)
        db_ses.add(course_to_save)
        db_ses.commit()
        return {"detail": "data stashed successfully"}
    except Exception as e:
        return {"detail": str(e)}


@kairos.post("/check")
def check_parameters_of_course(course_params: Course):
    return course_params


@kairos.delete("/delete/{course_id}")
def delete_course(course_id: int):
    try:
        course_to_delete = (
            db_ses.query(CoursesModel).filter_by(id=course_id).first()
        )
        db_ses.delete(course_to_delete)
        db_ses.commit()
        return {"detail": "success"}
    except UnmappedInstanceError:
        return {"detail": f"no course with id {course_id}"}
    except Exception as e:
        return {"detail": str(e)}


@kairos.get("/list")
def get_list_of_courses():
    all_courses = db_ses.query(CoursesModel).all()
    return (
        {"courses": all_courses, "count_of_courses": len(all_courses)}
        if all_courses
        else {"detail": "no courses", "count_of_courses": 0}
    )


@kairos.put("/edit/{course_id}")
def edit_course(course_id: int, course: CourseEdit):
    return course


@kairos.get("/course/{course_id}")
def get_course(course_id: int):
    try:
        course = db_ses.query(CoursesModel).filter_by(id=course_id).first()
        if course:
            return course
        return {"detail": f"no course with id {course_id}"}
    except Exception as e:
        return {"detail": str(e)}
