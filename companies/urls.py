from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('companies/', views.CompanyList.as_view(), name='companies-list'),
    path('companies/<int:pk>/', views.CompanyDetails.as_view(), name='companies-details'),

    path('companies/<int:pk>/employees/', views.EmployeeList.as_view(), name='employees-list'),
    path('companies/<int:pk>/employees/<int:pk>/', views.EmployeeDetails.as_view(), name='employees-details'),
]

urlpatterns= format_suffix_patterns(urlpatterns)

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),]