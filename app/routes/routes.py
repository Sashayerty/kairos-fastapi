from fastapi import APIRouter, Depends
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlmodel import Session, SQLModel, create_engine

from app.models import Courses

# from app.models.db_session import create_session, global_init
from app.schemas import (
    Course,
    CourseCreate,
    CourseEdit,
    CourseList,
    CourseSave,
)

# from app.models.courses_model import CoursesModel


# global_init("./database/kairos.db")
# db_ses = create_session()
kairos = APIRouter(tags=["General Endpoints"])
sqlite_file_name = "kairos.db"
sqlite_url = f"sqlite:///database/{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@kairos.on_event("startup")
def on_startup():
    create_db_and_tables()


@kairos.post("/gen")
def generate_course(course: CourseCreate):
    return {"hello": "world"}


@kairos.post("/save")
def save_course_to_database(
    course: Courses,
    session: Session = Depends(get_session),
):
    try:
        session.add(course)
        session.commit()
        return {"detail": "data stashed successfully"}
    except Exception as e:
        return {"detail": str(e)}


@kairos.post("/check")
def check_parameters_of_course(course_params: Course):
    return course_params


@kairos.delete("/delete/{course_id}")
def delete_course(
    course_id: int,
    session: Session = Depends(get_session),
):
    try:
        course_to_delete = session.get(Courses, course_id)
        session.delete(course_to_delete)
        session.commit()
        return {"detail": "success"}
    except UnmappedInstanceError:
        return {"detail": f"no course with id {course_id}"}
    except Exception as e:
        return {"detail": str(e)}


@kairos.get(
    "/list",
    response_model=CourseList,
)
def get_list_of_courses(
    session: Session = Depends(get_session),
):
    all_courses = session.query(Courses).all()
    return (
        {"courses": all_courses, "count_of_courses": len(all_courses)}
        if all_courses
        else {"courses": "no courses", "count_of_courses": 0}
    )


@kairos.put("/edit/{course_id}")
def edit_course(course_id: int, course: CourseEdit):
    return course


@kairos.get(
    "/course/{course_id}",
    response_model=Course,
)
def get_course(
    course_id: int,
    session: Session = Depends(get_session),
):
    try:
        course = session.query(Courses).filter_by(id=course_id).first()
        if course:
            return course
        return {"detail": f"no course with id {course_id}"}
    except Exception as e:
        return {"detail": str(e)}
