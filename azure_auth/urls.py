from django.urls import path

from azure_auth.views import azure_auth_callback, azure_auth_login, azure_auth_logout

app_name = "azure_auth"
urlpatterns = [
    path("sign_in", azure_auth_login, name="login"),
    path("sign_out", azure_auth_logout, name="logout"),
    path("redirect", azure_auth_callback, name="callback"),
]
