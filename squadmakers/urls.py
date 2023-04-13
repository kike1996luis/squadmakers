
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from jokes.views import UpdateJokesAPI, AddJokeAPI, RandomJokeAPI
from maths.views import LcmMathsAPI, PlusMathsAPI

schema_view = get_schema_view(
    openapi.Info(
        title="Prueba Técnica SquadMakers",
        default_version='v1',
        description="Swagger",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),

    # from django REST framework

    path('api/jokes/', UpdateJokesAPI.as_view(), name='Update and Get Jokes'),
    path('api/jokes/<str:type>/', RandomJokeAPI.as_view(), name='Add Jokes'),
    path('api/jokes/add', AddJokeAPI.as_view(), name='Add Joke'),
    path('api/math/lcm/', LcmMathsAPI.as_view(), name='Lcm Math'),
    path('api/math/plus/', PlusMathsAPI.as_view(), name='Plus one Math'),
]
