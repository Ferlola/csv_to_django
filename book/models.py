from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    used_books = models.FloatField()
    pages = models.PositiveIntegerField()
    avg_reviews = models.FloatField()
    n_reviews = models.CharField(max_length=200)
    star5 = models.CharField(max_length=5)
    star4 = models.CharField(max_length=5)
    star3 = models.CharField(max_length=5)
    star2 = models.CharField(max_length=5)
    star1 = models.CharField(max_length=5)
    dimensions = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    ISBN_13 = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    complete_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
