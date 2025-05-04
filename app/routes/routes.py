from fastapi import APIRouter
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.models.courses_model import CoursesModel
from app.models.db_session import create_session, global_init
from app.schemas import CourseSchema, CourseToDeleteSchema, CourseToSaveSchema

global_init("./database/kairos.db")
db_ses = create_session()
kairos = APIRouter(prefix="/kairos", tags=["General Endpoints"])


@kairos.post("/gen")
def generate_course():
    course = CoursesModel(theme="Python", course={})
    db_ses.add(course)
    db_ses.commit()
    return {"hello": "world"}


@kairos.put("/save")
def put_course_to_database(course: CourseToSaveSchema):
    return course


@kairos.post("/check")
def check_parameters_of_course(course_params: CourseSchema):
    return course_params


@kairos.delete("/delete")
def delete_course_by_id(course: CourseToDeleteSchema):
    try:
        course_to_delete = (
            db_ses.query(CoursesModel).filter_by(id=course.id).first()
        )
        db_ses.delete(course_to_delete)
        db_ses.commit()
        return {"detail": "success"}
    except UnmappedInstanceError:
        return {"detail": f"no course with id {course.id}"}
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
