__all__ = ['MODEL_URL', 'MODEL_VIEW']


MODEL_URL = """from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from {{ app }} import views

urlpatterns = [
{% for model in models %}
    path('{{ model | lower }}/', views.{{ model }}List.as_view()),
    path('{{ model | lower }}/<int:pk>/', views.{{ model }}Detail.as_view()),
{% endfor %}
]

urlpatterns = format_suffix_patterns(urlpatterns)
"""


MODEL_VIEW = """from rest_framework import generics
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}List(generics.ListCreateAPIView):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer

class {{ model }}Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
{% endfor %}"""
