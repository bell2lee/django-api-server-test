from django.db import models


class Feed(models.Model):
    content = models.TextField(null=False, verbose_name="내용")
    owner = models.CharField(null=False, verbose_name="작성자", max_length=12)
    created_at = models.DateTimeField(auto_now=True, null=True, verbose_name="작성일")

    class Meta:
        verbose_name_plural = "피드"