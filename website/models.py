from django.db import models

from django_ckeditor_5.fields import CKEditor5Field

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news_images/")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def short_content(self):
        """Returns a short snippet of the content for display."""
        return self.content[:100] + "..." if len(self.content) > 100 else self.content

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Trustee(models.Model):
    # Name of the trustee
    name = models.CharField(max_length=255)

    # Avatar/profile picture
    picture = models.ImageField(upload_to="trustee_avatars/", blank=True, null=True)

    # Position or role of the trustee
    position = models.CharField(max_length=255, blank=True, null=True)

    bio = CKEditor5Field("Bio", config_name="default", blank=True, null=True)

    class Meta:
        verbose_name = "Trustee"
        verbose_name_plural = "Board of Trustee"

    def __str__(self):
        return self.name


class Team(models.Model):
    # Name of the team member
    name = models.CharField(max_length=255)

    # Role of the team member
    role = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name
