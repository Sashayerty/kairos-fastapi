import json

from app import config
from app.mistral_ai_initializer import mistral_ai_initializer


def edit_course(course: dict, desires: str) -> dict:
    """Функция для эдитинга курса на основе правок
    Args:
        course (dict): Курс, который меняем
        desires (str): Правки

    Returns:
        dict: Измененный курс"""
    json_example = """
    {
        "1":{
                "title": "Как начать программировать",
                "data":  "Как можно подробно распиши пункт."
            },
        "1.1":
            {
                "title": "Азы и начала",
                "data":  "Как можно подробно распиши пункт."
            },
        "1.2":
            {
                "title": "Выбор языка",
                "data":  "Как можно подробно распиши пункт."
            },
        "2":
            {
                "title": "Основные языки программирования",
                "data":  "Как можно подробно распиши пункт."
            },
    }
    """
    prompt = f"""Привет! Ты редактор курсов по пожеланию пользователя. Твоя задача сделать с курсом именно то, что
    просит пользователь. Курс: {json.dumps(course)} Правки пользователя: {desires}. Вернуть нужно такой же по
    структуре курс, но с правками пользователя. Пример структуры курса: {json_example}"""
    client = mistral_ai_initializer()
    response = client.message(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=config.MISTRAL_DEFAULT_MODEL,
        temperature=0.1,
        response_format={
            "type": "json_object",
        },
    )
    return json.loads(response)
