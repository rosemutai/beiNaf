from django.db import models
from django.db import IntegrityError

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.email

class Deceased(models.Model):
    deceasedid = models.IntegerField(primary_key=True, unique=True)
    firstname = models.CharField(max_length=50)
    Middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50)
    Date_of_Birth = models.DateField()
    Date_of_death = models.DateField()
    Life_Description = models.TextField()
    funeral_arrangements = models.TextField(default="het")
    photo = models.ImageField()
    no_condolence = models.IntegerField(default=0)
   
    class Meta:
        verbose_name_plural = 'Deceased'


    def __str__(self):
        return self.firstname 

class CondolenceNotes(models.Model):
    deceasedid = models.ForeignKey(Deceased, related_name="condolences", null=True, blank=True, on_delete=models.CASCADE)
    condoled_by = models.CharField(max_length=200)
    message = models.TextField()
   

    def save(self, *args, **kwargs):
        self.deceasedid.no_condolence += 1
        print("Deceased:", self.deceasedid.firstname)
        self.deceasedid.save()
        super(CondolenceNotes, self).save(*args, **kwargs)


    def __str__(self):
        return  self.condoled_by

    class Meta():
        verbose_name_plural = 'Condolence Notes'


class DeceasedGallery(models.Model):
    deceasedid = models.ForeignKey(Deceased, related_name="image_gallery", on_delete=models.CASCADE)
    images = models.FileField(blank=True, upload_to = 'images/')

    def __str__(self):
        return self.deceasedid.firstname