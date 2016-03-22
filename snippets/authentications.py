"""Add custom authencation."""
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    """Example for custome authentication."""

    def authenticate(self, request):
        """Get authencate."""
        username = request.META.get('X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthencationFailed("No such user")

        return (user, None)
