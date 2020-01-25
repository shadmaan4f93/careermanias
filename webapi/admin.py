from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import  Coaching , CoachingFacultyMember,CoachingReview,CoachingMetaData
from .models import  Course ,Batch,Branch, Address,Geolocation                     

# Register your models here.
my_models = [Coaching,CoachingFacultyMember,CoachingReview,CoachingMetaData,
            Course ,Batch,Branch, Address,Geolocation
                ]
admin.site.register(my_models)
