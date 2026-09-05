from django.urls import path, include
from myapp import views
from .views import (maqola_list,
maqola_detail,mahsulot_list,mahsulot_detail,
home,api_maqolalar,maqola_search)
app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('maqolalar/',views.maqola_list,name='maqola_list'),
    path('maqolalar/<int:pk>/', views.maqola_detail, name='maqola_detail'),
    path('mahsulot/',views.mahsulot_list,name='mahsulot_list'),
    path('mahsulot/<slug:slug>/', views.mahsulot_detail, name='mahsulot_detail'),
    path('maqola-search/', views.maqola_search, name='maqola_search'),
    path('api-maqolalar/', views.api_maqolalar, name='api_maqolalar'),
]
