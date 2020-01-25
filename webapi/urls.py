from django.urls import path, re_path

from . import views

urlpatterns = [

    # coachings basic urls
    re_path(r'^coachings/create/$', view=views.SimpleCoachingCreateAPIView.as_view()),
    re_path(r'^coachings/detail/$', view=views.SimpleCoachingDetailView.as_view()),
    re_path(r'^coachings/all/$', view=views.SimpleCoachingListAPIView.as_view()),
    re_path(r'^coachings/search/$', view=views.CoachingSearchAPIView.as_view()),

    # coaching advance urls
    re_path(r'^coachings/detail/advance/$', view=views.AdvanceCoachingDetailView.as_view()),

    # branch urls
    re_path(r'^coachings/branch/create/', view=views.BranchCreateAPIView.as_view()), 
    re_path(r'^coachings/branch/update/(?P<pk>[\w\-]+)/$', view=views.BranchDetailView.as_view()), 


    # Address urls
    re_path(r'^coachings/address/create/', view=views.AddressCreateAPIView.as_view()), 
    re_path(r'^coachings/address/update/(?P<pk>[\w\-]+)/$', view=views.AddressDetailView.as_view()), 

    # Course urls
    re_path(r'^coachings/course/create/', view=views.CourseCreateAPIView.as_view()), 
    re_path(r'^coachings/course/update/(?P<pk>[\w\-]+)/$', view=views.CourseDetailView.as_view()), 


    # Batch urls
    re_path(r'^coachings/batch/create/', view=views.BatchCreateAPIView.as_view()), 
    re_path(r'^coachings/batch/update/(?P<pk>[\w\-]+)/$', view=views.BatchDetailView.as_view()), 

    # CoachingFacultyMember urls
    re_path(r'^coachings/faculty/create/', view=views.CoachingFacultyMemberCreateAPIView.as_view()), 
    re_path(r'^coachings/faculty/update/(?P<pk>[\w\-]+)/$', view=views.CoachingFacultyMemberDetailView.as_view()), 

    # CoachingMetaData
    re_path(r'^coachings/meta/create/', view=views.CoachingMetaDataCreateAPIView.as_view()), 
    re_path(r'^coachings/meta/update/(?P<pk>[\w\-]+)/$', view=views.CoachingMetaDataDetailView.as_view()), 
]