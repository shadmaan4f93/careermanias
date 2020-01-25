from django.conf.urls import url
from . import views as api_views

urlpatterns = [
    url(
        regex=r'^coaching/$',
        view=api_views.CoachingListAPIView.as_view(),
    )
]