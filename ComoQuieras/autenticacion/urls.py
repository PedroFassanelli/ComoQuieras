from django.urls import path

from .views import cerrar_sesion, iniciar_sesion
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password-reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-send.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name='password_reset_complete'),



]
