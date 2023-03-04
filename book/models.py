from django.db import models
# from datetime import timedelta

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    author = models.CharField(max_length= 100)
    stars = models.FloatField(default= 0)

class Member(models.Model):
    name = models.CharField(max_length= 100)
    # for consistency
    member_id = models.IntegerField()
    
class Borrowed(models.Model):
    member_id = models.ForeignKey(Member, on_delete= models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete= models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add= True)
    # idk id this script is correct
    # borrowed_until = models.DurationField(default= borrowed_at + timedelta(days= 30))
    # this must have a condition
    # being_borrowed = models.BooleanField(default= False)
    
