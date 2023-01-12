from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist_app.urls')),
    path('', todolist_app.index, name="index"),

    path('account/', include('account.urls')),

    path('contact/', todolist_app.contact, name='contact'),
    path('about/', todolist_app.about, name='about'),
]
