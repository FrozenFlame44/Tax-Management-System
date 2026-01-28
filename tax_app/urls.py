from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('file/', views.file_return, name='file_return'),
    path('receipt/<int:id>/', views.download_receipt, name='receipt'),
    path('pay/<int:return_id>/', views.make_payment, name='make_payment'),
]