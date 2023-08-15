from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import AdminView, CreateUserView, CustomTokenObtainPairView, LogoutView
# https://github.com/rg3915/gallery/blob/master/gallery
urlpatterns = [
    path('', csrf_exempt(CreateUserView.as_view())),
    path('admin/', AdminView.as_view(), name='user-list'),
    path('admin/<id>/', AdminView.as_view(), name='user-detail'),
    path('token/', CustomTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),

    # path('token/refresh/', TokenRefreshView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
