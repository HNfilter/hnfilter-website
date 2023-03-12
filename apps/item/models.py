from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    number_of_votes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s' % self.title


class Vote(models.Model):
    item = models.ForeignKey(Item, related_name='votes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.item.number_of_votes = self.item.number_of_votes + 1
        self.item.save()
        super(Vote, self).save(*args, **kwargs)

class Comment(models.Model):
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)

    body = models.TextField()

    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.item.number_of_comments = self.item.number_of_comments + 1
        self.item.save()
        super(Comment, self).save(*args, **kwargs)
