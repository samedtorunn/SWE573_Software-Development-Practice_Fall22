from django.test import TestCase
from .forms import UserRegistrationForm
from .models import Post, UserProfile, Comment, Space
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegistrationFormTestCase(TestCase):
    def test_form_validation(self):
        # Test a valid form submission
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test an invalid form submission (passwords do not match)
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'invalid'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())



class PostModelTest(TestCase):
    def setUp(self):
        # Create a test Post object
        self.test_post = Post(title='Test Post', content='This is a test post')
        self.test_post.save()

    def test_post_title(self):
        # Test that the title of the test Post object is correct
        self.assertEqual(self.test_post.title, 'Test Post')

    def test_post_content(self):
        # Test that the content of the test Post object is correct
        self.assertEqual(self.test_post.content, 'This is a test post')


class SpaceModelTestCase(TestCase):
    def setUp(self):
        # Create a test space
        self.test_admin = UserProfile.objects.create(id=1, user=User.objects.create(username='admin'))
        self.test_space = Space.objects.create(
            admin=self.test_admin,
            title='Test Space',
            slug='test-space'
        )

    def test_space_str_representation(self):
        # Test the string representation of a Space object
        self.assertEqual(str(self.test_space), 'Test Space')

    def test_space_admin(self):
        # Test the admin field of a Space object
        self.assertEqual(self.test_space.admin, self.test_admin)