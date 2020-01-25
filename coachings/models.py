
import uuid
from django.db import models
from phone_field import PhoneField
from django_mysql.models import ListCharField

# Create your models here.

class Coaching(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250,unique=True,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    logo = models.ImageField(upload_to='logos/',blank=True , null=True)
    logo_link = models.URLField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    Type_CHOICES = (
        ('Main', 'Main'),
        ('Sub', 'Sub')
    )

    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250,blank=False,null=False,verbose_name='coaching_branch_name')
    coaching = models.ForeignKey(Coaching, related_name = 'branches',on_delete=models.CASCADE)
    branch_type = models.CharField(max_length=250,blank=False,null=False,
                                    verbose_name='coaching_branch',choices=Type_CHOICES, default="Main"
                                        )
    
    def __str__(self):
        return self.name

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    branch = models.OneToOneField(Branch,related_name='address_of',on_delete=models.CASCADE)
    line1 = models.CharField(max_length=250,blank=False,null=False)
    line2 = models.CharField(max_length=250,blank=True,null=True)
    apartment = models.CharField(max_length=250,blank=True,null=True)
    building = models.CharField(max_length=250,blank=True,null=True)
    landmark = models.CharField(max_length=250,blank=True,null=True)
    district = models.CharField(max_length=250,blank=False,null=False,default=None)
    state = models.CharField(max_length=250,blank=False,null=False,default=None)
    pincode = models.CharField(max_length=250,blank=False,null=False,default=None)


class Geolocation(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    address = models.OneToOneField(Address,related_name='location_of',on_delete=models.CASCADE)
    lat = models.DecimalField(decimal_places=2,max_digits=2,null=False,default=None)
    lng = models.DecimalField(decimal_places=2,max_digits=2,null=False,default=None)
    region = models.IntegerField()
    subregion = models.IntegerField()

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250,blank=False,null=False,verbose_name='branch_course_name')
    branch = models.ForeignKey(Branch,related_name='courses_of',on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    start_date = models.DateField(editable=True)
    end_date   = models.DateField(editable=True)
    syllabus   = models.FileField(blank=True,null=True)
    fees       = models.DecimalField(blank=False,null=False,max_digits=2,decimal_places=2,default=None)
    currency   = models.CharField(max_length=30,blank=True,null=False,default="INR")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CoachingFacultyMember(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    coaching = models.ForeignKey(Coaching,related_name="faculty_of",on_delete=models.CASCADE)
    name = models.CharField(max_length=250,blank=False,null=False)
    age  = models.PositiveIntegerField()
    specialization = models.CharField(max_length=250,blank=False,null=False)
    meta_description = models.TextField(blank=True,null=True)
    faculty_image = models.ImageField(upload_to='faculties/',blank=True , null=True)
    faculty_image_link = models.URLField()

class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250,blank=False,null=False,verbose_name='course_batch_name')
    course = models.ForeignKey(Course,related_name='batches_of',on_delete=models.CASCADE)
    teacher = models.ForeignKey(CoachingFacultyMember,related_name='teaches',on_delete=models.CASCADE,null=False,blank=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    student_limit = models.PositiveIntegerField(blank=True,null=True)
    students_enrolled = models.PositiveIntegerField(blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CoachingReview(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    coaching = models.ForeignKey(Coaching,related_name='reviews_of',on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=250,blank=True,null=True)


class CoachingMetaData(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    coaching = models.ForeignKey(Coaching,related_name="metadata_of",on_delete=models.CASCADE)
    contact = PhoneField(blank=False,default=None, help_text='coaching phone number')
    help_contact = PhoneField(blank=True,default=None, help_text='coaching phone number')
    owner_name = models.CharField(max_length=250,blank=True,null=True)
    owner_description = models.TextField(blank=True,null=True)
    owner_image = models.ImageField(upload_to='owners/',blank=True , null=True)
    owner_image_link = models.URLField()
    established_on = models.DateField(blank=True,null=True)














    


