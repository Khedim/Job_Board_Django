from django.urls import path
from .views import job_list, job_detail, add_job
from .api import job_list_api, job_detail_api, add_job_api, JobList, JobDetail

app_name = 'job'
urlpatterns = [
	path('', job_list, name='job_list'),
	path('add/', add_job, name='add-job'),
	path('api/', job_list_api, name='job-list-api'),
	path('api/add/', add_job_api, name='add-job-api'),
	path('api/list-add/', JobList.as_view(), name='list-add-job-api'),
	path('api/job-rud/<str:slug>/', JobDetail.as_view(), name='job-rud-api'),
	path('api/<str:slug>/', job_detail_api, name='job-detail-api'),
	path('<str:slug>/', job_detail, name='job_detail')
]
