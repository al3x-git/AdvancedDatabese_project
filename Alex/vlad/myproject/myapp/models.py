from django.db import models
# Create your models here.


def uploads(instance, filename):
    return 'myapp/image/{}'.format(filename)


class CreatedUpdated(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SocialIssue(CreatedUpdated):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=uploads)
    description = models.TextField()

    def __str__(self):
        return self.title
