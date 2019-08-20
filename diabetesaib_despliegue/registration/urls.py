#Una vez configurado la url del proyecto raíz, se debe indicar el de registro tal y como aparece
from django.urls import path
from .views import SignUpView

urlpatterns=[
    path('signup/', SignUpView.as_view(), name="signup")
]