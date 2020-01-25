from rest_framework import serializers

from coachings.models import Coaching

class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaching
        fields = ('name','id','description')

