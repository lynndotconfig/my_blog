"""snippet/models.py."""
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.core.exceptions import ValidationError


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICE = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICE = sorted((item, item) for item in get_all_styles())


def validate_file(filefield_obj):
        """Validate file size."""
        content_types = ['video/x-msvideo', 'video/mp4']
        megabyte_limit = 50.0
        try:
            content_type = filefield_obj.content_type
            if content_type in content_types:
                if filefield_obj._size > megabyte_limit * 1024 * 1024:
                    raise ValidationError(
                        "Max file size is %s MB" % str(megabyte_limit))
            else:
                raise ValidationError(
                    "File type not supported")
        except AttributeError:
            pass
        return


class Snippet(models.Model):
    """model snippet."""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True, default='', max_length=100)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICE, default='friendly', max_length=50)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        """Ordering."""

        ordering = ('created',)

    def save(self, *args, **kwargs):
        """Rewrite save method.

        Use the 'pygments' library to create a highlighted HTML representation
        of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class Experiment(models.Model):
    """Example for file upload in rest."""

    notes = models.TextField(blank=True)
    samplesheet = models.FileField(
        upload_to='snippets/uploads/%Y/%m/%d',
        blank=True, default='',
        validators=[validate_file])
    user = models.ForeignKey('auth.user', related_name='experiments')
    code = models.TextField(blank=True)


class Profile(models.Model):
    """Example for testing TemplateHTMLRenderer."""

    name = models.CharField(max_length=50)


class Album(models.Model):
    """Model for example of Serializer stringRelatedField."""

    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        """Print object."""
        return '%d: %s' % (self.id, self.album_name)


class Track(models.Model):
    """Track of album."""

    album = models.ForeignKey(Album, related_name='tracks')
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        """Meta."""

        unique_together = ('album', 'order')
        ordering = ['order']

    def __str__(self):
        """Print str."""
        return '%d: %s' % (self.order, self.title)
