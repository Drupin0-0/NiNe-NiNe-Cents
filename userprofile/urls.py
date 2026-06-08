from django.urls import path
from userprofile.views import userprofile_view
urlpatterns = [
    path('', userprofile_view, name='userprofile.view')
]