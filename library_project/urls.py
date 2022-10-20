from django.contrib import admin
# Include is used by the books app 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main url file to include urls from books app. "" shows that the user will be redirected to the books urls
    path('', include("books.urls")),
    
    # URL path for the API
    path("api/", include("apis.urls")),
]
