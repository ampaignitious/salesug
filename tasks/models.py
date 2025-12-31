from django.db import models

# Create your models here.
class Task(models.Model):
    status_choices=[
        ('Pending','Pending'),
        ('Closed','Closed')
    ]
    name = models.CharField(max_length=10)
    description=models.TextField(max_length=300)
    created_at =models.DateTimeField(auto_now_add=True)
    task_status=models.CharField(
        # max_length=1,
        choices=status_choices,
        default='Pending'
    )

    def __str__(self):
        return self.name