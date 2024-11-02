from django.db import models

"""
    class Post
        -id:int
        -title:varchar
        -body:text
        -created_at:datetime
        -modified_at:datime
"""

class Post(models.Model):    # noqa: F811
    id = models.IntegerField(primary_key=True)    # noqa: F811
    title = models.CharField(max_length=50)    # noqa: F811
    body = models.TextField()    # noqa: F811
    created_at = models.DateTimeField(auto_now_add=True)    # noqa: F811
    modified_at = models.DateTimeField(auto_now=True)    # noqa: F811
