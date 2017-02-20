from django.conf.urls import include, url
from django.contrib import admin

from inventory import views as inventory_index

urlpatterns = [
    # Examples:
    # url(r'^$', 'rudra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', inventory_index.index, name='index'),
    url(r'^item/(?P<id>\d+)/', inventory_index.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
