from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('', views.index, name='index'),
   path('add/', views.add, name='add'),
   path('add/add_record/', views.add_record, name='add_record'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('update/<int:id>', views.update, name='update'),
   path('update/update_record/<int:id>', views.update_record, name='update_record')
]

urlpatterns += staticfiles_urlpatterns()