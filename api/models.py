from django.db import models

# Create your models here.

class blackcoffer(models.Model):
        end_year=models.TextField(max_length=4,default='unknown')
        intensity=models.TextField(max_length=3,default='unknown')
        sector=models.TextField(max_length=30,default='unknown')
        topic=models.TextField(max_length=20,default='unknown')
        insight=models.TextField(max_length=150,default='unknown')
        url=models.TextField(max_length=500,default='unknown')
        region=models.TextField(max_length=50,default='unknown')
        start_year=models.TextField(max_length=4,default='unknown')
        impact=models.TextField(max_length=50,default='unknown')
        added=models.TextField(max_length=40,default='unknown')
        published=models.TextField(max_length=40,default='unknown')
        country=models.TextField(max_length=40,default='unknown')
        relevance=models.TextField(max_length=3,default='unknown')
        pestle=models.TextField(max_length=20,default='unknown')
        source=models.TextField(max_length=200,default='unknown')
        title=models.TextField(max_length=500,default='unknown')
        likelihood=models.TextField(max_length=3,default='unknown')