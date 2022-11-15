from django.db import models

# Create your models here.


class FUpload(models.Model):
    filef = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)

class BUpload(models.Model):
    fileb = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)

class PUpload(models.Model):
    filep = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)

class BankStatement(models.Model):
    text = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, blank=True)
    statement = models.FileField(upload_to='files/',)

    def __str__(self):
        return str(self.pk)

class Resume(models.Model):
    file = models.FileField(upload_to='files/',)

    def __str__(self):
        return str(self.pk)