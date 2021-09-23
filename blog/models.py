from django.db import models
from django.contrib.auth.models import User

# Create your models here.




from django.db import models

class Blogs(models.Model):
    content = models.CharField(max_length=1024, null=True, blank=True)
    header = models.CharField(max_length=1024, null=True, blank=True)
    image = models.CharField(max_length=1024, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  related_name='author')
    liked_users = models.ManyToManyField(User, default=list, null=True, blank=True, related_name='liked_emails')
    
    class Meta:
        db_table = 'blogs'

    def __str__(self):
        return '{} {}'.format(self.id, self.author.email)


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from_token')
    token = models.CharField(max_length=1024)
    is_valid = models.BooleanField(default=False)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return '{} {} {}'.format(self.id, self.user.email, self.token)




