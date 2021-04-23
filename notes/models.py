from django.db import models

class Note(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
  text = models.TextField()

  def __str__(self):
    return "%s: %s" % (self.author.username, self.title)
