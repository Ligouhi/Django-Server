from django.db import models

# Create your models here.
class User(models.Model):

    ID = models.CharField(max_length=36,primary_key='True')
    Password = models.CharField(max_length=20,null='Flase')
    Plan = models.CharField(max_length=20,null='Flase')


class Passage(models.Model):
    Name = models.CharField(max_length=36, primary_key='True')
    Author = models.CharField(max_length=20)
    Econtent = models.CharField(max_length=6000, null='Flase')
    Ccontent = models.CharField(max_length=6000, null='Flase')
    From =  models.ForeignKey("Album",to_field="Name",on_delete=models.CASCADE)

class Album(models.Model):
    Name = models.CharField(max_length=36, primary_key='True')
    Pnum = models.CharField( max_length=36,null='Flase')
    Img = models.CharField( max_length=36,null='Flase')

class Collect(models.Model):
    ID = models.ForeignKey('User',on_delete=models.CASCADE)
    Pname = models.ForeignKey('Album',on_delete=models.CASCADE)

class Note(models.Model):
    ID = models.ForeignKey('User',on_delete=models.CASCADE)
    Passage = models.ForeignKey('Passage',on_delete=models.CASCADE)
    Note = models.CharField( max_length=200,null='Flase')