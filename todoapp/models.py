from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('grocery', 'Grocery'),
        ('study', 'Study'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    title= models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    complete= models.BooleanField(default=False)
    create= models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)  # Adding the due_date field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
