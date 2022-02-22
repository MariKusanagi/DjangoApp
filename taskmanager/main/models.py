from django.db import models


class Task(models.Model):
    title = models.CharField("title", max_length=50)
    task = models.TextField("description")

    def __str__(self):
        return self.title

    class Mate:
        verbose_name = "task"
        verbose_name_plural = "tasks"
