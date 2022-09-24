from django.db import models
from library_management.models import UserAccount
# Create your models here.


TYPE = (
    ('STUDENT','STUDENT'),
    ('TEACHER','TEACHER')
)
class CollageModel(models.Model):
    user = models.OneToOneField(to=UserAccount, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE,max_length=8)
    dept = models.CharField(max_length=100, blank=True, null=True)
    student_class = models.CharField(max_length=100, blank=True, null=True)