from django.urls import path
from . import views

urlpatterns = [
    # VIEW
    path('', views.overview, name='overview'),
    path('siswa/', views.siswaList, name='siswa-list'),
    path('tugas/', views.tugasList, name='tugas-list'),
    path('siswa-detail/<str:pk>/', views.siswaDetail, name='siswa-detail'),
    path('tugas-detail/<str:pk>/', views.tugasDetail, name='tugas-detail'),

    # CREATE
    path('siswa-create/', views.siswaCreate, name='siswa-create'),
    path('tugas-create/', views.tugasCreate, name='tugas-create'),

    # UPDATE
    path('siswa-update/<str:pk>/', views.siswaUpdate, name='siswa-update'),
    path('tugas-update/<str:pk>/', views.tugasUpdate, name='tugas-update'),

    # DELETE
    path('siswa-delete/<str:pk>/', views.siswaDelete, name='siswa-delete'),
    path('tugas-delete/<str:pk>/', views.tugasDelete, name='tugas-delete'),
]
