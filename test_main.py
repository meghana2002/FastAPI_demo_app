import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app, get_posts, add_post, user_login, verify_token

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.posts = [
            {"id": 1, "title": "Post 1", "content": "Content 1"},
            {"id": 2, "title": "Post 2", "content": "Content 2"},
            {"id": 3, "title": "Post 3", "content": "Content 3"},
        ]

    def test_get_posts(self):
        with patch('main.posts', self.posts):
            response = self.client.get("/posts")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"data": self.posts})

    def test_user_login_valid_credentials(self):

        user_data = {"email": "test@example.com", "password": "password123"}
        with patch('main.check_user', return_value=True):
            response = self.client.post("/user/login", json=user_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["user"], user_data)

    def test_user_login_invalid_credentials(self):
        user_data = {"email": "test@example.com", "password": "password123"}
        with patch('main.check_user', return_value=False):
            response = self.client.post("/user/login", json=user_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"error": "Invalid Login credentials"})

    def test_verify_token_valid_token(self):
        token = "valid_token"
        with patch('main.decodeJWT', return_value={"email": "test@example.com"}):
            response = self.client.get("/user/verify-token?token=" + token)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "valid": True,
                "user": {"email": "test@example.com"}
            })

    def test_verify_token_invalid_token(self):
        token = "invalid_token"
        with patch('main.decodeJWT', return_value=None):
            response = self.client.get("/user/verify-token?token=" + token)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"valid": False})

    def test_add_post(self):
        new_post = {"title": "New Post", "content": "New Content"}
        with patch('main.posts', self.posts):
            with patch('main.jwtBearer.verify_jwt', return_value=True):  # Mock token verification
                response = self.client.post("/posts", json=new_post, headers={"Authorization": "Bearer valid_token"})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), {
                    "info": "Post Added!",
                    "data": {"id": 4, "title": "New Post", "content": "New Content"}
                })


if __name__ == '__main__':
    unittest.main()
