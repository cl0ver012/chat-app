from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import apps.public.views, apps.chat.views

urlpatterns = [
    path('', apps.public.views.index_page),
    path('profile', apps.public.views.profile, name='profile'),
    path('login', apps.public.views.login_view, name='login'),
    path('register', apps.public.views.register_view, name='register'),
    path('profile/my-room', apps.public.views.my_room, name='my_room'),
    path('chat/', include('apps.chat.urls'), name='chat'),
    path('api/user/', include('apps.public.api_urls')),
    path('api/chat/', include('apps.chat.api_urls')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)