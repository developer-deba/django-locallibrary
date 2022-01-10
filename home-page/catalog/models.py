from django.db import models
from django.db.models.base import Model
from django.urls import reverse
import uuid
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre")
    def __str__(self) :
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summery = models.TextField(max_length=1000,help_text='enter brief description of the book')
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    genre = models.ManyToManyField(Genre,help_text='Select a genre of the book')
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'
    def __str__(self):
        return self.title
    def get_absolute_urls(self):
        return reverse('book detail', args=[str(self.id)])

class Bookinstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text='unique id for book')
    due_back = models.DateTimeField(null=True,blank=True)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Avilable'),
        ('r','Reserd')
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS,default='m',blank=True,help_text='Book Availability')
    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return f'{self.id}({self.book.title})'
        
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField('Died',null=True, blank=True)
    class Meta:
        ordering = ['first_name','last_name']
    def get_absolute_urls(self):
        return reverse('author detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.first_name},{self.last_name}'
