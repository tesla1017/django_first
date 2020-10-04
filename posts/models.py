from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title #管理画面でTitleを表示させる。

    def summary(self):
        return self.body[:30]
