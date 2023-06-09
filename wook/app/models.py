from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField("名稱", max_length=70)
    subject = models.CharField("標題", max_length=220)
    content = models.TextField("內容")
    publication_date = models.DateTimeField("留言日期", auto_now_add=True)

    def __str__(self):
        return self.subjec