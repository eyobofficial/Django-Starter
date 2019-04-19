from django.test import TestCase

from accounts.models import Profile
from .factories import UserFactory


class CreateUserProfileTests(TestCase):
    """
    Tests for `create_user_profile` signal
    """

    def test_create_user_profile(self):
        """
        Ensure creating a new user also creates an associated
        profile
        """
        user = UserFactory()
        self.assertEqual(Profile.objects.filter(user=user).count(), 1)
