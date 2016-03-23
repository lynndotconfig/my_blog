"""Custom database-backend session engine.

to use this custom session engine just to change settings
"SESSION_ENGINE='project/app/sessions.py'"
"""
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.session.base_session import AbstractBaseSession
from django.db import models


class CustomSession(AbstractBaseSession):
    """CustomSession."""

    account_id = models.IntegerField(null=True, db_index=True)

    class Meta:
        """Meta."""

        app_lablel = 'mysessions'

    @classmethod
    def get_session_store_class(cls):
        """Get store class."""
        return SessionStore


class SessionStore(DBStore):
    """Custom sessionstore."""

    @classmethod
    def get_model_class(cls):
        """Get session class."""
        return CustomSession

    def create_model_instance(self, data):
        """Add account id to create instance."""
        obj = super(SessionStore, self).create_model_instance(self, data)
        try:
            account_id = int(data.get('_auth_user_id'))
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id
        return obj
