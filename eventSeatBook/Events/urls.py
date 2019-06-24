from django.urls import path
from . import views
from django.contrib.auth import urls

urlpatterns = [
	path('', views.events, name='events'),
	path('<int:id>', views.dete, name='dete'),
	path('register/<int:id>', views.register, name='register'),
 	path('adminpageabcd',views.adminpage, name='adminpage'),
 	path('adminform',views.addevent, name='addevent'),   
 	path('delete/<int:id>', views.delete_event, name='delete'),
 	path('deletor/<int:id>', views.deletor, name='delete_button'),
 	path('update/<int:id>', views.updater, name='update_button'),
 	path('stdlist/<str:Branch>', views.stdlist.as_view(), name='stdlist'),
 	path('stdlist2/<str:year>', views.stdlistt.as_view(), name='stdlist2'),
 	path('std', views.stdsearch, name='stdsearch'),
 	path('login/', views.login, name='login'),
 	path('studentupdate/<int:id>', views.presenter, name='present_button'),
 	#path('student', views.stddet, name='student'),
]