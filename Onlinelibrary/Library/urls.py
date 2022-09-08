from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('regis', views.regis, name='regis'),
    path('forgetpass', views.forgetpass, name='forgetpass'),
    path('course', views.course, name= 'course'),
    path('classroom', views.classroom, name='classroom'),
    path('classroom1', views.classroom1, name='classroom1'),
    path('intermediate', views.intermediate, name='intermediate'),
    path('higher', views.higher, name='higher'),
    path('college',views.college, name='college'),
    path('literature', views.literature, name='literature'),
    path('story', views.story, name='story'),
    path('indianlaw', views.indianlaw, name='indianlaw'),
    path('yoga', views.yoga, name='yoga'),
    path('spiritual', views.spiritual, name='spiritual'),
    path('diploma', views.diploma, name='diploma'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)