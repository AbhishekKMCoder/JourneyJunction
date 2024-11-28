from django.db import models

# Create your models here.



# AdminApp/models.py

class TourDestination(models.Model):
    Name = models.CharField(max_length=250)
    Location = models.CharField(max_length=300)
    Description = models.TextField()
    LongDescription = models.TextField(null=True, blank=True)
    Price = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    Nights = models.IntegerField(default=1)
    Image = models.ImageField(upload_to="destination_image", null=True, blank=True)  # destination_image folder
    title = models.CharField(max_length=200, default='Untitled')  # Add a default value
    star = models.CharField(max_length=60, null=True, blank=True)

    Activity1 = models.CharField(max_length=200, null=True, blank=True)
    Activity2 = models.CharField(max_length=200, null=True, blank=True)
    Activity3 = models.CharField(max_length=200, null=True, blank=True)
    Activity4 = models.CharField(max_length=200, null=True, blank=True)
    Activity5 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.Name



# class TourDestination(models.Model):
#     Name = models.CharField(max_length=250)
#     Location = models.CharField(max_length=300)
#     Description = models.TextField()
#     LongDescription = models.TextField(null=True, blank=True)
#     Price = models.CharField(max_length=100)
#     Duration = models.CharField(max_length=100)
#     Nights = models.IntegerField(default=1)
#     Image = models.ImageField(upload_to="destination_image", null=True, blank=True)
#
#
#
#     title = models.CharField(max_length=200, default='Untitled')  # Add a default value
#     star = models.CharField(max_length=60,null=True, blank=True)
#
#     Activity1 = models.CharField(max_length=200, null=True, blank=True)
#     Activity2 = models.CharField(max_length=200, null=True, blank=True)
#     Activity3 = models.CharField(max_length=200, null=True, blank=True)
#     Activity4 = models.CharField(max_length=200, null=True, blank=True)
#     Activity5 = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return self.Name


class HotelBookingModels(models.Model):
    HotelName = models.CharField(max_length=100)
    HotelRating = models.FloatField()
    HotelPrice = models.DecimalField(max_digits=10, decimal_places=2)
    HotelLocation = models.CharField(max_length=300)
    HotelDescription = models.TextField()
    HotelImage = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    HotelLink = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.HotelName





