from django.db import models
from ckeditor.fields import RichTextField
class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField
    gender=models.CharField(max_length=32)
    birthday=models.DateField()
    email=models.EmailField()
    adress=RichTextField()
    photo=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
class ArticleType(models.Model):
    label=models.CharField(max_length=32)
    description=RichTextField()
    def __str__(self):
        return self.label
class Article(models.Model):
    title=models.CharField(max_length=32)
    article_author=models.ForeignKey(to=Author,on_delete=models.CASCADE)
    description=RichTextField()
    content=RichTextField()
    article_type=models.ManyToManyField(to=ArticleType)
    public_time=models.DateField(auto_now=True)
    picture=models.ImageField(upload_to='images')
    click=models.IntegerField(default=0)
    recommend=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    email=models.EmailField()

# Create your models here.
