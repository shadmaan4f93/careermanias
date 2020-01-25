from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from coachings.models import (
    Coaching
)

from .serializers import (
    CoachingSerializer,
)

class CoachingListAPIView(ListAPIView):
    serializer_class = CoachingSerializer
    queryset = Coaching.objects.all()
