from django.contrib import admin
from django.urls import include, path

from .api import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/auth/", include("djoser.urls.authtoken")),
]
# comando para obter credenciais de autenticação:
# curl -X POST -d '{"username": "admin","password": "deco1234"}' \
# -H 'Content-Type: application/json' \
# http://127.0.0.1:8000/api/auth/token/login/
