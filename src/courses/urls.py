from django.urls import path
from .views import (
    CourseCreateView,
    CourseUpudateView,
    CourseDeleteView,
    CourseView,
    CourseListView,
    MyListFilterView
    #my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('',CourseListView.as_view(),name='courses-list'),
    #path('',CourseView.as_view(),name='courses-list'),
    #path('',CourseView.as_view(template_name='contact.html'),name='courses-list'),
    #path('',my_fbv,name='course-list'),
    #path('',MyListFilterView.as_view(),name='courses-list'), #used for filter data
    
    path('create/',CourseCreateView.as_view(),name='courses-create'),
    path('<int:id>',CourseView.as_view(),name='courses-detail'),
    path('<int:id>/update/',CourseUpudateView.as_view(),name='courses-update'),
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='courses-delete'),
]