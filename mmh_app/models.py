from django.db import models

# Create your models here.

class HomeOwner(models.Model):
    phone = models.CharField(max_length=13, primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    user = models.BooleanField(default=True)
    email = models.CharField(max_length=50)



class Architect(models.Model):
    phone = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=50)
    specilization = models.CharField(max_length=250)



class Contractor(models.Model):
    phone = models.CharField(max_length=13 , primary_key=True)
    name = models.CharField(max_length=50)
    expertise = models.CharField(max_length=250)



class Supplier(models.Model):
    phone = models.CharField(max_length=13 , primary_key=True)
    name = models.CharField(max_length=50)
    categloge = models.CharField(max_length=150)



class Manager(models.Model):
    phone = models.CharField(max_length=13, primary_key=True)
    password = models.CharField(max_length=50)
    user = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)



class ProjectManagement(models.Model):
    projectID = models.CharField(max_length=30 , primary_key=True)
    homeowner = models.ForeignKey(HomeOwner, on_delete=models.CASCADE)
    architech = models.ForeignKey(Architect, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    timeline = models.CharField(max_length=50)
    budget = models.CharField(max_length=50)
    progress = models.CharField(max_length=50)



class ServiceRequest(models.Model):
    homeowner = models.ForeignKey(HomeOwner, on_delete=models.CASCADE)
    architech = models.ForeignKey(Architect, on_delete=models.CASCADE, default="")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, default="")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    request_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)



class Feedback(models.Model):
    name = models.CharField(max_length=50, default='Annonymous')
    email = models.CharField(max_length=50, default='')
    remark = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']



class Catalogue(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='pics')
    quantity = models.CharField(max_length=50)


class Projects(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='contracts')
    ratings = models.CharField(max_length=50, default='*****')


class Design(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='pics')
    category = models.CharField(max_length=50)