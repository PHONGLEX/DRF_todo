from rest_framework.test import APITestCase

from authentication.models import User


class TestModel(APITestCase):

	def test_creates_user(self):
		user = User.objects.create_user('cryce', 'crycetruly@gmail.com', 'password123!@')
		self.assertIsInstance(user, User)
		self.assertFalse(user.is_staff)
		self.assertEqual(user.email, 'crycetruly@gmail.com')

	# def test_creates_super_user(self):
	# 	user1 = User.objects.create_superuser('cryce1', 'crycetruly1@gmail.com', 'password123!@')
	# 	print(user1, 'asdfasdf')
	# 	# self.assertIsInstance(user1, User)
	# 	self.assertFalse(user1.is_staff)
	# 	self.assertEqual(user1.email, 'crycetruly@gmail.com')

	def test_raises_error_when_no_username_is_supplied(self):
		self.assertRaises(ValueError, User.objects.create_user,username='',email='crycetruly@gmail.com',password='password123!@')

	def test_raises_error_with_message_when_no_username_is_supplied(self):
		with self.assertRaisesMessage(ValueError, "The given username must be set"):
			User.objects.create_user(username='', email='crycetruly@gmail.com', password='password123!@')

	def test_raises_error_when_no_email_is_supplied(self):
		self.assertRaises(ValueError, User.objects.create_user,username='crycetruly',email='',password='password123!@')

	def test_raises_error_with_message_when_no_email_is_supplied(self):
		with self.assertRaisesMessage(ValueError, "The given email must be set"):
			User.objects.create_user(username='crycetruly', email='', password='password123!@')
