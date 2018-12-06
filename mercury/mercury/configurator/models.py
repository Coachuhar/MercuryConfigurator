import datetime

from django.db import models
from django.utils import timezone


#Formula model 
class Formula(models.Model):
    lens = models.CharField(max_length=100)
    focal_length = models.CharField(max_length=20)
    brand = models.CharField(max_length=200)
    nominal_format = models.CharField(max_length=200)
    max_coverage = models.CharField(max_length=200)
    intended_camera = models.CharField(max_length=200)
    camera_class = models.CharField(max_length=200)
    mount = models.CharField(max_length=200)
    flange_distance = models.CharField(max_length=200)
    rear_element = models.CharField(max_length=200)
    lens_kit_no = models.CharField(max_length=50)
    focus_unit = models.CharField(max_length=200)
    shutter_plate = models.CharField(max_length=200)
    front_spacer = models.CharField(max_length=200)
    barrel_length = models.CharField(max_length=200)
    rs_20 = models.CharField(max_length=200)
    rs_30 = models.CharField(max_length=200)
    rs_40 = models.CharField(max_length=200)
    rs_60 = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)
    filter_size = models.CharField(max_length=200)
    shutter = models.CharField(max_length=200)
    image_circle = models.CharField(max_length=200)
    fov_35mm = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.lens_kit_no)

    
 #Model to hold components 
 # TODO maybe change the paypal_code to a foreign key    
class Component(models.Model):
    item_name = models.CharField(max_length=200)
    item_number = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    special_shipping = models.IntegerField(default=0)
    paypal_code = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.item_name

#Medium system lenses model
class System_lens_medium(models.Model):
    lens_system = models.CharField(max_length=100)
    shutter= models.CharField(max_length=100)
    shutter2 = models.CharField(max_length=100, default="none")
    shutter3 = models.CharField(max_length = 100, default="none")
    bolt_length = models.CharField(max_length=100)
    bolt_length2 = models.CharField(max_length = 100, default="none")
    bolt_length3 = models.CharField(max_length = 100, default="none")
    washers = models.CharField(max_length=100)
    washers2 = models.CharField(max_length = 100, default="none")
    washers3 = models.CharField(max_length = 100, default="none")
    front_spacer = models.CharField(max_length=100)
    front_spacer2 = models.CharField(max_length = 100, default="none")
    front_spacer3 = models.CharField(max_length = 100, default="none")
    spacer_ring = models.CharField(max_length = 100)
    spacer_ring2 = models.CharField(max_length = 100, default="none")
    spacer_ring3 = models.CharField(max_length = 100, default="none")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.lens_system
        
#135 mm system lens models 
class System_lens_135(models.Model):
    lens_system = models.CharField(max_length = 100)
    shutter = models.CharField(max_length=100)
    merc_body = models.CharField(max_length=200)
    merc_body2 = models.CharField(max_length = 100, default="none")
    shutter_spacer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lens_system

class Configuration(models.Model):
    camera_format = models.CharField(max_length = 100)
    lens_type = models.CharField(max_length = 100)
    lens_number = models.CharField(max_length = 100)
    focus_unit = models.CharField(max_length = 100)
    rs_value = models.CharField(max_length = 100)
    front_panel = models.CharField(max_length = 100)
    back_adapter = models.CharField(max_length = 100)
    back = models.CharField(max_length = 100)

    def __str__ (self):
        return self.lens_number

#class Paypal(models.Model):
    
#class Images(models.Model):
    
    


