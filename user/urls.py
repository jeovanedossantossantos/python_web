from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns

from user.views import CreateUserView,UserViewPrivate,AdminView,LogoutView,CustomTokenObtainPairView
# https://github.com/rg3915/gallery/blob/master/gallery
urlpatterns = [
    path('', csrf_exempt(CreateUserView.as_view())),
    path("token/",CustomTokenObtainPairView.as_view()),
    path("edite/",UserViewPrivate.as_view()),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("admin/",AdminView.as_view(), name="user-list"),
    path("admin/<id>/",AdminView.as_view(),name="user-detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
