from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlmodel import Session, SQLModel, create_engine

from app.ai_core import censor, cool_prompt, get_theory, plan
from app.models import Courses
from app.schemas import (
    Course,
    CourseCreate,
    CourseEdit,
    CourseList,
    ResponseSchema,
)

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
def generate_course(
    course: CourseCreate,
    response: Response,
):
    theme, desires, description_of_user = (
        course.theme,
        course.desires_of_user,
        course.description_of_user,
    )
    from_censor = censor(
        theme_from_user=theme,
        desires=desires,
    )
    if not from_censor["data"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": from_censor["reason"]}
    prompt = cool_prompt(
        users_theme=theme,
        desires=desires,
        description_of_user=description_of_user,
    )
    course_plan = plan(
        prompt_from_llm=prompt,
    )
    created = get_theory(
        prompt_from_prompt_agent=prompt,
        plan=course_plan,
    )
    created_course = Course(
        theme=theme,
        desires_of_user=desires,
        description_of_user=description_of_user,
        course=created,
    )
    return created_course


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
