from django.urls import path
from lists.views import home_page, view_list

urlpatterns = [
    path('', home_page),
    path('lists/<int:list_id>/', view_list),
]