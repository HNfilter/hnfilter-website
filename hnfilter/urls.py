from django.contrib import admin
from django.urls import path

# SMA: import all views here
from django.contrib.auth import views # built-in django view
from apps.core.views import signup
from apps.item.views import frontpage, submit, newest, vote, item_detail, search
from apps.userprofile.views import userprofile, votes, submissions

urlpatterns = [
    # core app
    path('signup/', signup, name='signup'),

    # item app
    path('', frontpage, name='frontpage'),
    path('item/<int:item_id>/vote', vote, name='vote'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('newest', newest, name='newest'),
    path('search', search, name='search'),
    path('submit/', submit, name='submit'),
    path('login/',views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    # userprofile app
    path('u/<str:username>/', userprofile, name='userprofile'),
    path('u/<str:username>/votes', votes, name='votes'),
    path('u/<str:username>/submissions', submissions, name='submissions'),
]
