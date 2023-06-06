from main import Repository, User, Category, Post, Hashtag, Role


class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def create_user(self, name, email, password):
        user = User(name=name, email=email, password=password)
        self.repository.add_user(user)

    def get_user_by_id(self, user_id):
        user = self.repository.get_user_by_id(user_id)
        return user


class PostService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def create_post(self, user_id, title, content, category_id):
        user = self.repository.get_user_by_id(user_id)
        category = self.repository.get_category_by_id(category_id)
        post = Post(title=title, content=content, user=user, category=category)
        self.repository.add_post(post)

    def get_post_by_id(self, post_id):
        post = self.repository.get_post_by_id(post_id)
        return post

    # Другие методы Use Case для работы с постами


# Создание экземпляр репозитория
repository = Repository()

# Создание экземпляры служб Use Case Layer
user_service = UserService(repository)
post_service = PostService(repository)

# Пример использования Use Case Layer
user_service.create_user("John Doe", "john@example.com", "password")
user = user_service.get_user_by_id(1)
print(user.name, user.email)

post_service.create_post(user_id=1, title="New Post", content="Lorem ipsum", category_id=1)
post = post_service.get_post_by_id(1)
print(post.title, post.content)
