import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_data(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), "Hello, World!")
        
    def test_hello_devops_status_code(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
    
    def test_hello_devops_data(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode('utf-8'), "Hello, DevOps World!")

if __name__ == '__main__':
    unittest.main()
