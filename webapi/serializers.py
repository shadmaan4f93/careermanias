from rest_framework import serializers

from webapi.models import Coaching,CoachingFacultyMember,CoachingMetaData,CoachingReview
from webapi.models import Address,Geolocation,Batch,Branch,Course

# simple independent serializers for models


class CoachingMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingMetaData
        fields = ('owner_name','owner_description','established_on','contact')


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('id','lat','lng')

# 
class AddressSerializer(serializers.ModelSerializer):
    location_of = GeolocationSerializer(many=False, read_only=True)
    class Meta:
        model = Address
        fields = ('id','location_of','line1','line2','building','landmark','district','state','pincode','branch')

# 
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('name','id','start_time','end_time','student_limit','students_enrolled','is_active')

# 
class CoachingFacultyMemberSerializer(serializers.ModelSerializer):
    batches_of = BatchSerializer(many=True, read_only=True)
    class Meta:
        model = CoachingFacultyMember
        fields = ('name','id','age','specialization','meta_description','batches_of')

# 
class CourseSerializer(serializers.ModelSerializer):
    batches_of = BatchSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('name','id','description','start_date','end_date','fees','is_active','batches_of')

# 
class BranchSerializer(serializers.ModelSerializer):
    address_of = AddressSerializer(many=False, read_only=True)
    courses_of = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = ('name','id','branch_type','courses_of','address_of')

# 
class AdvanceCoachingSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, read_only=True)
    faculty_of = CoachingFacultyMemberSerializer(many=True, read_only=True)
    class Meta:
        model = Coaching
        fields = ('name','id','description','branches','faculty_of')

# 
class SimpleCoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaching
        fields = ('name','id','description', 'logo_link')