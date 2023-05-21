from django.urls import path
from home.api.views import *

urlpatterns = [
    path('categories/', categoriesView, name="categories_api"),
    path('categories/<slug:slug>', categoryViewSlug, name="categories_api_slug"),
    path('activities/', activitiesView, name="activities_api"),
    path('activities/<slug:slug>', activityViewSlug, name="activities_api_slug"),
    path('blogs/', BlogsView.as_view(), name="blogs_api"),
    path('blogs/<slug:slug>', BlogViewSlug.as_view(), name="blogs_api_slug"),
    path('teachers/', TeachersView.as_view(), name="teachers_api"),
    path('teachers/<slug:slug>', TeacherViewSlug.as_view(), name="teachers_api_slug"),
]
