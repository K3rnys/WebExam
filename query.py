from app import app
from models import db, Genre
"""
genres = [
    'Биография', 'Детектив', 'Детская литература', 'Драма', 'История',
    'Комедия', 'Любовный роман', 'Мемуары', 'Научная литература', 'Поэзия',
    'Приключения', 'Психология', 'Публицистика', 'Роман', 'Саморазвитие',
    'Сатира', 'Триллер', 'Ужасы', 'Фантастика', 'Фэнтези', 'Энциклопедия'
]

with app.app_context():
    db.session.query(Genre).delete()  # удаляет всё
    for name in genres:
        db.session.add(Genre(name=name))
    db.session.commit()
    print("Жанры обновлены!")
"""