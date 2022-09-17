"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """Test creating user with an email"""
        email = "testemail@test.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test email is normalised for new users."""
        sameple_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]

        for email, expected_email in sameple_emails:
            user = get_user_model().objects.create_user(
                email=email,
            )
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='test_pass'
            )

    def test_create_super_user(self):
        """Test to create a super user."""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test_pass',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
