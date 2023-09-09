from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TarefaView
# https://github.com/rg3915/gallery/blob/master/gallery
urlpatterns = [
    path('', TarefaView.as_view()),
    path("<id>/",TarefaView.as_view())
   
]
urlpatterns = format_suffix_patterns(urlpatterns)
