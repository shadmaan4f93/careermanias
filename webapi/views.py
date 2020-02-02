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
from django.db.models import Q
from webapi.utils import GeolocationApi
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


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
    
    serializer_class = SimpleCoachingSerializer
    pagination_class = SmallResultsSetPagination
    

    def get_queryset(self):
        """
        Optionally restricts the returned coaching to a given user,
        by filtering against a `city` `stream` `fees`query parameter in the URL.
        """
        coachings_pk = []
        queryset = Coaching.objects.all()
        print(self.request.query_params)
        course = self.request.query_params.get('course')
        fee    = self.request.query_params.get('feet')
        course_queryset = Course.objects.filter(Q(fees__lte=int(fee))|Q(stream__contains='science'))[:5]
        if course_queryset is not None:
            for course in course_queryset:
                course_branch_caoching_pk = course.branch.coaching.id
                coachings_pk.append(course_branch_caoching_pk)
            coaching_queryset = Coaching.objects.filter(pk__in=coachings_pk)
        queryset = coaching_queryset
        
        return queryset

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

# class AddressCreateAPIView(CreateAPIView):
#     serializer_class = AddressSerializer
#     queryset = Address.objects.all()
    
class AddressCreateAPIView(APIView):
    def post(self, request, format=None):
        """
        creates Address and location together
        """
        success = False
        try:
            line1=request.data["line1"]
            district=request.data["district"]
            state=request.data["state"]
            pincode=request.data["pincode"]
            branch=request.data["branch"]
            address_obj = Address(line1=line1,district=district,
                                state=state,pincode=pincode,branch=Branch.objects.get(pk=branch))
            address_obj.save()
            address_string = district+", "+state+", "+pincode
            if address_obj.id:
                location_coordinates = GeolocationApi.get_lat_lng(address_string)
                geolocation_obj = Geolocation(address=address_obj,
                                        lat=location_coordinates["latitude"],
                                        lng=location_coordinates["latitude"])
                geolocation_obj.save()
                success=True
        except Exception as e:
            success=False
            print(e)
        return Response(success)

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



def save_location_at_create_address(self,request):
    print(self,request)

