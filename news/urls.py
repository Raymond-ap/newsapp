from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.entertainment, name="home"),
    path('entertainment/<int:pk>/',
         views.EntertainmentDetail.as_view(), name="news_deatil"),
    path('sport/<int:pk>/', views.SportDetail.as_view(), name="sport_deatil"),
    path('lifestyle/<int:pk>/', views.LifeStyleDetail.as_view(), name="lifestyle"),
    path('technogies/<int:pk>/', views.TechnologyDetail.as_view(), name="techs"),
    path('health/<int:pk>/', views.HealthDetail.as_view(), name="health"),
    path('business/<int:pk>/', views.BusinessDetail.as_view(), name="business"),
    path("breaking/<int:pk>/",
         views.BreakingNewsDetail.as_view(), name="breakingNews"),
    path('technology/', views.allTechNews, name="technology"),
    path('health/', views.allHealth, name="health"),
    path('entertainments/', views.allEntertain, name="news_deatil"),
    path('sports/', views.allSports, name="sports"),
    path('lifeStyle/', views.allLifeSytle, name="lifeStyle"),
    path('celebs/', views.allCelebs, name="celebs"),
    path('celebrity/<str:name>/', views.getCeleb, name="celebrities"),
    path('business/', views.allBussiness, name="business"),
    path('contact/', views.contactUs, name="contact"),
    path('breaking_news/', views.breakingNews, name="breaking_news")

]
