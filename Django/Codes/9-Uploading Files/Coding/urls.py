from django.urls import include, path
from Coding import views

urlpatterns = [
    path('', views.index),  # default page

    path('any_file', views.any_file),
    path('message', views.message),
    path('multiple_files', views.multiple_files),
    path('particular_file', views.particular_file),
    path('specific_size_file', views.sized_file),
    path('upload_any_file', views.upload_any_file),
    path('upload_multiple_files', views.upload_multiple_files),
    path('upload_particular_format_file', views.upload_particular_format_file),
    path('upload_specific_size_file', views.upload_specific_size_file),
    path('view_files/<type>', views.view_files),
    path('download_file', views.download_file),
    path('delete_file', views.delete_file),
    path('ajax_file', views.ajax_file),
    path('upload_ajax_file', views.upload_ajax_file),
    path('ajax_multiple_files', views.ajax_multiple_files),
    path('upload_ajax_multiple_files', views.upload_ajax_multiple_files),
    path('view_ajax_files/<type>', views.view_ajax_files),
    path('download_ajax_file', views.delete_ajax_file),
    path('delete_ajax_file', views.delete_ajax_file),
]