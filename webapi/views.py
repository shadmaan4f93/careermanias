from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from webapi.models import (
    Coaching,CoachingFacultyMember,CoachingReview,CoachingMetaData,
            Course ,Batch,Branch, Address,Geolocation
)

from webapi.serializers import (
    AddressSerializer,BatchSerializer,CoachingFacultyMemberSerializer,CourseSerializer,
    BranchSerializer,AdvanceCoachingSerializer,SimpleCoachingSerializer,CoachingMetaDataSerializer
)


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


# coachings basic api

class SimpleCoachingCreateAPIView(CreateAPIView):
    serializer_class = SimpleCoachingSerializer
    queryset = Coaching.objects.all()

class SimpleCoachingListAPIView(ListAPIView):
    serializer_class = SimpleCoachingSerializer
    queryset = Coaching.objects.all()
    pagination_class = SmallResultsSetPagination

class SimpleCoachingDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SimpleCoachingSerializer
    queryset = Coaching.objects.all()

class CoachingSearchAPIView(ListAPIView):
    queryset = Coaching.objects.all()
    serializer_class = SimpleCoachingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']

# caoching advance api

class AdvanceCoachingDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvanceCoachingSerializer
    queryset = Coaching.objects.all()

# Branch     
class BranchCreateAPIView(CreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

class BranchDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    
# Address
class AddressCreateAPIView(CreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class AddressDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
# Course
class CourseCreateAPIView(CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
# Batch
class BatchCreateAPIView(CreateAPIView):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()

class BatchDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()
# CoachingFacultyMember

class CoachingFacultyMemberCreateAPIView(CreateAPIView):
    serializer_class = CoachingFacultyMemberSerializer
    queryset = CoachingFacultyMember.objects.all()

class CoachingFacultyMemberDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CoachingFacultyMemberSerializer
    queryset = CoachingFacultyMember.objects.all()

# CoachingMetaData

class CoachingMetaDataCreateAPIView(CreateAPIView):
    serializer_class = CoachingMetaDataSerializer
    queryset = CoachingMetaData.objects.all()

class CoachingMetaDataDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CoachingMetaDataSerializer
    queryset = CoachingMetaData.objects.all()




