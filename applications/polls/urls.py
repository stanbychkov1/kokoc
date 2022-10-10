from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', views.PollView.as_view(), name='poll'),
    path('rating/', views.RatingView.as_view(), name='rating'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('items/<int:pk>/', views.ItemBuyView.as_view(), name='item_buy'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('unsuccess/', views.SuccessView.as_view(), name='unsuccess')
]
