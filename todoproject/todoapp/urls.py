
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classview/',views.tasklistview.as_view(),name='classview'),
    path('classview1/<int:pk>/',views.taskdetailview.as_view(),name='classview1'),
    path('classview2/<int:pk>/',views.taskupdateview.as_view(),name='classview2'),
    path('classview3/<int:pk>/',views.taskdeleteview.as_view(),name='classview3'),
]
