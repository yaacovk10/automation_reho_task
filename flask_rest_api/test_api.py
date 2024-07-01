import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/users'

class TestUserAPI(unittest.TestCase):

    def test_get_all_users_positive(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('data', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('total', data)
        self.assertIn('total_pages', data)

    def test_get_all_users_negative(self):
        # Negative test by accessing a page number that does not exist
        response = requests.get(f'{BASE_URL}?page=9999')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), 0)  # Expect no users for a non-existent page


    def test_get_single_user_positive(self):
        response = requests.get(f'{BASE_URL}/1')
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertIn('first_name', user)
        self.assertIn('last_name', user)
        self.assertIn('email', user)
        self.assertIn('avatar', user)

    def test_get_single_user_negative(self):
        response = requests.get(f'{BASE_URL}/9999')  # Assuming 9999 is an invalid ID
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'User not found')


    def test_create_user_positive(self):
        new_user = {
            'first_name': 'Alice',
            'last_name': 'Baba',
            'email': 'alice.baba@reqres.in.com',
            'avatar': 'https://reqres.in/img/faces/4-image.jpg'
        }
        response = requests.post(BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 201)
        user = response.json()
        self.assertIn('id', user)
        self.assertEqual(user['first_name'], 'Alice')
        self.assertEqual(user['last_name'], 'Baba')
        self.assertEqual(user['email'], 'alice.baba@reqres.in.com')
        self.assertEqual(user['avatar'], 'https://reqres.in/img/faces/4-image.jpg')
        self.assertIn('createdAt', user)
        self.assertIn('updatedAt', user)

    def test_create_user_negative(self):
        # Negative test with missing required fields
        new_user = {
            'name': 'Incomplete User'  # Missing email
        }
        response = requests.post(BASE_URL, json=new_user)
        print(response.status_code)
        self.assertEqual(response.status_code, 400)  # Expecting a 400 Bad Request
        data = response.json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Invalid user data')  # Assumes API returns this message


    def test_update_user_positive(self):
        updated_user = {'name': 'Alice Updated', 'email': 'alice_updated@reqres.in.com'}
        response = requests.put(f'{BASE_URL}/1', json=updated_user)
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user['name'], 'Alice Updated')
        self.assertEqual(user['email'], 'alice_updated@reqres.in.com')
        self.assertIn('updatedAt', user)


    def test_update_user_negative(self):
        updated_user = {'name': 'Nonexistent User'}
        response = requests.put(f'{BASE_URL}/9999', json=updated_user)  # Assuming 9999 is an invalid ID
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'User not found')



    def test_delete_user_positive(self):
        # Adding a user first to delete
        new_user = {
            'first_name': 'To Be Deleted',
            'last_name' : 'Also To Be Deleted',
            'email': 'delete@example.com',
            'avatar': 'https://reqres.in/img/faces/4-image.jpg'
        }
        response = requests.post(BASE_URL, json=new_user)
        created_user = response.json()
        user_id = created_user['id']

        # Now delete the created user
        response = requests.delete(f'{BASE_URL}/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'User deleted')

    def test_delete_user_negative(self):
        response = requests.delete(f'{BASE_URL}/9999')  # Assuming 9999 is an invalid ID
        self.assertEqual(response.status_code, 404)  # Assuming delete returns 404 for non-existent user
        data = response.json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'User not found')

if __name__ == '__main__':
    unittest.main()
