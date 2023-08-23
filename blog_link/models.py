from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


CONDITION = ((0, "Draft"), (1, "Published"))

class Resource(models.Model):
    """
    Model class for resources added to the blog_link
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    url = models.URLField(default="")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resourse_added"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    site_screenshot = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    condition = models.IntegerField(choices=CONDITION, default=0)
    admirers = models.ManyToManyField(
        User, related_name="admirers_like", blank=True
    )
    tags = TaggableManager()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.admirers.count()
    

class CommentResourse(models.Model):
    """
    Model class for comments added to the blog_link
    """
    post = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_field = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_field} by {self.name}"



