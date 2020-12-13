from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home ,name='home'),
    path('contact/',views.contact ,name='contact'),
    path('userlogin/',views.userlogin, name='userlogin'),
    path('signup/',views.signup, name='signup'),
    path('userlogout/',views.userlogout, name='userlogout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='home/password_reset.html'),name='reset_password'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),name='password_reset_complete'),

]
