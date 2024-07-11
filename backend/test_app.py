import unittest
import json
from app_init import create_app, db
from app.models import User, Property, Review

class PropertyManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

        with self.app.app_context():
            db.create_all()

            # Create a test user
            user = User(username='testuser', email='testuser@example.com', password_hash='testpassword', role='host')
            db.session.add(user)
            db.session.commit()
            
            # Create a test property
            property = Property(name='Test Property', description='Test Description', address='123 Test Address', host_id=user.id)
            db.session.add(property)
            db.session.commit()

            # Create a test review
            review = Review(content='Test Review', rating=5, user_id=user.id, property_id=property.id)
            db.session.add(review)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def get_auth_token(self):
        login_response = self.client.post('/api/login', data=json.dumps({
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data.decode())['token']
        return token

    def test_create_property(self):
        token = self.get_auth_token()
        response = self.client.post('/api/properties', data=json.dumps({
            'name': 'New Property',
            'description': 'New Description',
            'address': '456 New Address'
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Property created successfully!', str(response.data))

    def test_edit_property(self):
        token = self.get_auth_token()
        response = self.client.put('/api/properties/1', data=json.dumps({
            'name': 'Updated Property',
            'description': 'Updated Description'
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Property updated successfully!', str(response.data))

    def test_delete_property(self):
        token = self.get_auth_token()
        response = self.client.delete('/api/properties/1', headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Property deleted successfully!', str(response.data))

    def test_add_review(self):
        token = self.get_auth_token()
        response = self.client.post('/api/reviews', data=json.dumps({
            'content': 'New Review',
            'rating': 4,
            'property_id': 1
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Review added successfully!', str(response.data))

    def test_edit_review(self):
        token = self.get_auth_token()
        response = self.client.put('/api/reviews/1', data=json.dumps({
            'content': 'Updated Review',
            'rating': 5
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Review updated successfully!', str(response.data))

    def test_display_reviews(self):
        response = self.client.get('/api/reviews')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Review', str(response.data))

if __name__ == '__main__':
    unittest.main()
