from abc import ABC, abstractmethod
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound


Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass


class SQLAlchemyRepository(Repository):
    def __init__(self):
        self.session = Session()

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()

    def get_by_id(self, obj_id, obj=None):
        try:
            return self.session.query(obj.__class__).filter_by(id=obj_id).one()
        except NoResultFound:
            return None

    # Другие методы репозитория


# Определите свои модели данных с помощью SQLAlchemy и унаследуйтесь от Base


# Пример модели данных User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    # Добавьте остальные поля


# Создайте таблицы в базе данных, если они еще не существуют
Base.metadata.create_all(engine)

repository = SQLAlchemyRepository()

# Пример использования репозитория
user = User(name='John', email='john@example.com')
repository.add(user)

retrieved_user = repository.get_by_id(user.id)
print(retrieved_user.name, retrieved_user.email)
