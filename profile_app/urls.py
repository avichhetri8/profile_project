from django.urls import path

from profile_app.views import HelloApiView

urlpatterns = [
    path('', HelloApiView.as_view(), name='hello')
]
