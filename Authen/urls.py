 
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from Authen import views
from Authen.forms import LoginForm, MyPasswordResetForm, PasswordChangeForm, MyPasswordSetForm

urlpatterns = [
    path('Register/', views.CustomerRegistrationView.as_view(), name="Register"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='Authen/login.html', authentication_form=LoginForm), name="login"),
    
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='Authen/password_change.html', form_class=PasswordChangeForm, success_url='/authentication/passwordChangedone'),  name="password_change"),
    
    path('passwordChangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='Authen/password_change_done.html'), name="password_change_done"),
    
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name="logout"),
    
    
    # reset password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='Authen/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='Authen/password_reset_done.html'), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='Authen/password_reset_confirm.html', form_class=MyPasswordSetForm), name="password_reset_confirm"),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='Authen/password_reset_complete.html'), name="password_reset_complete"),

]
 