from django.db import models
from django.urls import reverse
import users.models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(users.models.User, on_delete=models.CASCADE)
    upvoters = models.ManyToManyField(users.models.User, related_name="upvoted_questions")
    downvoters = models.ManyToManyField(users.models.User, related_name="downvoted_questions")
    tags = models.ManyToManyField("Tag")
    @property
    def vote(self):
        return self.upvoters.count() - self.downvoters.count()


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Answer(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(users.models.User, on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    upvoters = models.ManyToManyField(users.models.User, related_name="upvoted_answers")
    downvoters = models.ManyToManyField(users.models.User, related_name="downvoted_answers")
    @property
    def vote(self):
        return self.upvoters.count() - self.downvoters.count()