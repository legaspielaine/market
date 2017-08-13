from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='homepage'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<username_id>[0-9]+)/$', views.profile, name='profile'),

    url(r'^login/$', auth_views.login, name='login'),

    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^admin/$', admin.site.urls),

    # add an item
    url(r'^item/add/$', views.ItemCreate.as_view(success_url="/home/"), name='item-add'),

    # update an item
    url(r'item/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name='item-update'),

    # url(r'^(?P<username_id>[0-9]+)/$', views.ItemCreate.as_view(), name='item-add'),

    # delete an item
    # url(r'item/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name='item-delete'),

]

# urlpatterns = [
#     url(r'^$', views.HomeView.as_view(), name='home'),
#
#     url(r'^(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
#
#     # url(r'^home/add/$', views.ProfileView.as_view(), name='item-add'),
# ]






