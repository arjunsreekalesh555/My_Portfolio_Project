from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index-page'),
   path('add-bio/', views.addBio, name='add_bio'),
   path('view-bio/', views.viewBio, name='view_bio'),
   path('add-certificates/', views.addCertificates, name='add_certificates'),
   path('view-certificates/', views.viewCertificates, name='view_certificates'),
   path('add-projects/', views.addProjects, name='add_projects'),
   path('view-projects/', views.viewProjects, name='view_projects'),
   path('update-bio/<int:data_id>/', views.updateBio, name='update_bio'),
   path('contacts/', views.Contacts, name='contacts'),
   path('delete-project/<int:project_id>/', views.deleteProject, name='delete_project'),
   path('delete-certificate/<int:certificate_id>/', views.deleteCertificate, name='delete_certificate'),
   path('project-details/<int:project_id>/', views.projectDetails, name='project_details'),
   path('certificate-details/<int:certificate_id>/', views.certificateDetails, name='certificate_details'),

]