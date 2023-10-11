from django.db import models

class Bug(models.Model):
    BUG_TYPES = (
        ('error', 'Error'),
        ('new_feature', 'New Feature'),
    )

    STATUS = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    description = models.TextField()
    bug_type = models.CharField(max_length=25, choices=BUG_TYPES)
    report_date = models.DateTimeField()
    status = models.CharField(max_length=25, choices=STATUS)

    def __str__(self):
        return self.description