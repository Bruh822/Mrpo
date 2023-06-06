from datetime import datetime
from dataclasses import dataclass


class Hashtag:
    def __init__(self, hashtag_id: int, post: Post):
        self.hashtag_id = hashtag_id
        self.post = post


class User:
    def __init__(self, user_id: int, name: str, second_name: str, phone: str, email: str, password: str, address: str, hashtag: Hashtag):
        self.user_id = user_id
        self.name = name
        self.second_name = second_name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.hashtag = Hashtag


class Category:
    def __init__(self, category_id: int, name: str):
        self.category_id = category_id
        self.name = name

class Post:
    def __init__(self, post_id: int, full_text: str, title: str, date: datetime, author: str, category: Category, user: User):
        self.post_id = post_id
        self.full_text = full_text
        self.title = title
        self.date = date
        self.author = author
        self.category = category
        self.user = user


class Role:
    def __init__(self, role_id: int, role_type: str, user: User):
        self.role_id = role_id
        self.role_type = role_type
        self.user = user


class Repository:
    def __init__(self):
        self.users = []
        self.categories = []
        self.posts = []
        self.hashtags = []
        self.roles = []

    # Методы для добавления экземпляров сущностей в репозиторий

    def add_user(self, user):
        self.users.append(user)

    def add_category(self, category):
        self.categories.append(category)

    def add_post(self, post):
        self.posts.append(post)

    def add_hashtag(self, hashtag):
        self.hashtags.append(hashtag)

    def add_role(self, role):
        self.roles.append(role)

    # Методы для получения экземпляров сущностей из репозитория

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_category_by_id(self, category_id):
        for category in self.categories:
            if category.category_id == category_id:
                return category
        return None

    def get_post_by_id(self, post_id):
        for post in self.posts:
            if post.post_id == post_id:
                return post
        return None

    def get_hashtag_by_id(self, hashtag_id):
        for hashtag in self.hashtag:
            if hashtag.hashtag_id == hashtag_id:
                return hashtag
        return None


    def get_role_by_id(self, role_id):
        for role in self.roles:
            if role.role_id == role_id:
                return role
        return None

"""
4 лаба
"""
@dataclass(frozen=True) #1 задание
class User:
    user_id: int
    name: str
    second_name: str
    phone: str
    email: str
    password: str
    address: str
    hashtag: Hashtag


@dataclass(frozen=True)
class Category:
    category_id: int
    name: str


@dataclass(frozen=True)
class Post:
    post_id: int
    full_text: str
    title: str
    date: datetime
    author: str
    category: Category
    user: User


@dataclass(frozen=True)
class Hashtag:
    hashtag_id: int
    post: Post


@dataclass(frozen=True)
class Role:
    role_id: int
    role_type: str
    user: User

class Repository: #2 задание
    def __init__(self):
        self.users = []
        self.categories = []
        self.posts = []
        self.hashtags = []
        self.roles = []

    def __eq__(self, other):
        if isinstance(other, Repository):
            return (
                self.users == other.users and
                self.categories == other.categories and
                self.posts == other.posts and
                self.hashtags == other.hashtags and
                self.roles == other.roles
            )
        return False

"""
Правило 1: Пользователи могут иметь несколько ролей, но каждая роль относится только к одному пользователю.

Правило 2: Категории должны иметь уникальные идентификаторы.

Правило 3: Посты должны содержать уникальные идентификаторы и быть связаны с одной категорией.

Правило 4: Хэштеги должны иметь уникальные идентификаторы и быть связаны с одним постом.
"""

def validate_user_roles(repository): #3 задание
    user_roles = {}
    for role in repository.roles:
        user = role.user
        if user in user_roles:
            user_roles[user].append(role)
        else:
            user_roles[user] = [role]
    for user, roles in user
