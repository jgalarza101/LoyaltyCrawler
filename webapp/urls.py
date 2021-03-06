from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html')),
    path('get_session/<int:session_id>/', views.get_session, name='get_session'),
    path('artifact/<int:artifact_id>/', views.view_artifact, name='view_artifact'),
    path('criteria', views.get_search_criteria, name='get_search_criteria'),
    path('criteria/add/<str:new_criterion>/', views.add_search_criteria, name='add_search_criteria'),
    path('criteria/remove/<str:criterion_to_remove>/', views.remove_search_criteria, name='remove_search_criteria'),
    path('start_session/', views.start_session, name='start_session'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
    path('check_last_session_index/', views.check_last_session_index, name='check_last_session_index'),
]

# As a final step, create a file inside your catalog folder called urls.py,
# and add the following text to define the (empty) imported urlpatterns.
# This is where we'll add our patterns as we build the application.
