import random
from django.db import models

from library_management.models import UserAccount

# Create your models here.
LANGUAGE = (
    ('hindi','hindi'),
    ('english','english')
)

FORMAT = (
    ('DVD','DVD'),
    ('PDF','PDF'),
    ('DOC','DOC')
)

EDITION = (
    ('First_Edition','First_Edition'),
    ('Second_Edition','Second_Edition'),
    ('Third_Edition','Third_Edition'),
    ('Fourth_Edition','Fourth_Edition')
)

class BookModel(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13,unique=True,blank=True)
    summary = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, choices=LANGUAGE,blank=True,null=True)
    genre = models.CharField(max_length=100,blank=True, null=True)
    topic = models.CharField(max_length=100, blank=True, null=True)
    edition = models.CharField(max_length=20,choices=EDITION,blank=True, null=True)
    formate = models.CharField(max_length=10,choices=FORMAT,blank=True, null=True)
    publisher = models.CharField(max_length=500,blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    book = models.FileField(upload_to='book/',blank=True,null=True)
    book_cover = models.ImageField(upload_to='book_cover/',blank=True, null=True)

    def save(self, *args, **kwargs):
        self.isbn = random.randrange(1000000000000, 9999999999999)
        super(BookModel, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title