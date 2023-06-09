from django.db import models


class user_registration(models.Model):
    #fields of our table.
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    
    def __str__(self):

        return '%s %s %s %s %s %s' % (self.fname, self.lname, self.
                                      email, self.mobile, self.password, self.address)
