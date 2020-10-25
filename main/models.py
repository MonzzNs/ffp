from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Item(models.Model):
    title = models.CharField(_("Item Name"), max_length=250, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Visitor(models.Model):
    username = models.CharField(_("Username"), max_length=50)
    user_id = models.CharField(_("User ID"), max_length=15, blank=True)
    password = models.CharField(_("Password"), max_length=50)
    
    def __str__(self):
        return self.username
    
class CarouselImg(models.Model):
    img = models.ImageField(_("Carousel Images"), upload_to="carousel img/")
    