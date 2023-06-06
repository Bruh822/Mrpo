import unittest
from datetime import datetime
from xml.dom.minidom import Entity

from main import Repository, User, Category, Post, Hashtag, Role


class RepositoryServiceTests(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()

    def test_add_user(self):
        user = User(user_id=1, name='John', second_name='Doe', phone='123456789', email='john@example.com',
                    password='password', address='123 Street', hashtag=None)

        self.repository.add_user(user)

        self.assertIn(user, self.repository.users)

    def test_get_user_by_id(self):
        user = User(user_id=1, name='John', second_name='Doe', phone='123456789', email='john@example.com',
                    password='password', address='123 Street', hashtag=None)
        self.repository.add_user(user)

        retrieved_user = self.repository.get_user_by_id(1)

        self.assertEqual(user, retrieved_user)


class EntityServiceTests(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()
        # Можно добавить необходимую инициализацию объектов сущностей

    def test_entity_equal(self):
        # Проверяем, что два экземпляра сущности равны
        entity1 = Entity(entity_id=1, name='Entity')
        entity2 = Entity(entity_id=1, name='Entity')

        self.assertEqual(entity1, entity2)

    def test_entity_not_equal(self):
        # Проверяем, что два экземпляра сущности не равны
        entity1 = Entity(entity_id=1, name='Entity 1')
        entity2 = Entity(entity_id=2, name='Entity 2')

        self.assertNotEqual(entity1, entity2)


if __name__ == '__main__':
    unittest.main()
