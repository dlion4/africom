from django.urls import reverse, path, include


from . import views

urlpatterns = [
    path("", views.AfricomHomeView.as_view(), name="home"),
    path("about/",views.AfricomAboutView.as_view(), name="about"),
]
