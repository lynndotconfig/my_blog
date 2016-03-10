"""my_blog Custom Exceptions.

Examples:
    try:
        self.live = Snippet.objects.get(pk=self.select_id)
    except Snippet.DoesNotExist:
        raise BadSnippetId
"""

from rest_framework.exceptions import APIException


class BadSnippetId(APIException):
    """Exceptions for search snippet by id."""

    status_code = 400
    default_detail = "Snippet id does not exist."
