from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# VIEW

@api_view(['GET'])
def overview(request):
   
    overview = {
        'siswa':'/siswa/',
        'tugas':'/tugas/',
    }
    return Response(overview)

@api_view(['GET'])
def siswaList(request):
    siswa = Siswa.objects.all()
    serializer = SiswaSerializer(siswa, many=True)  # many di berikan True karena disini kita ingin agar semua object di tabel siswa di tampilkan


    return Response(serializer.data)    # disini kita isi .data karena agar diconvert dalam bentuk json, jika tidak isi akan error

@api_view(['GET'])
def tugasList(request):
    tugas = Tugas.objects.all()
    serializer = TugasSerializer(tugas, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def siswaDetail(request, pk):
    siswa = Siswa.objects.get(id=pk)
    serializer = SiswaSerializer(siswa, many=False) # many di berikan False karena disini kita ingin agar satu data saja yang ditampilnya

    return Response(serializer.data)


@api_view(['GET'])
def tugasDetail(request, pk):
    tugas = Tugas.objects.get(id=pk)
    serializer = TugasSerializer(tugas, many=False)

    return Response(serializer.data)
    
# CREATE

@api_view(['POST'])
def siswaCreate(request):
    
    # untuk create kita beri parameter data dan pass request.data, request.data disini mirip dengan request.POST, hanya saja untuk api, request.data lebih powerful untuk rest api
    # request.data juga akan mengirimkan JSON object
    # source: https://www.django-rest-framework.org/tutorial/2-requests-and-responses/

    serializer = SiswaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def tugasCreate(request):
    
    serializer = TugasSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE

@api_view(['POST'])
def siswaUpdate(request, pk):
    siswa = Siswa.objects.get(id=pk)
    serializer = SiswaSerializer(instance=siswa, data=request.data) # tambahkan instance untuk update data siswa tertentu

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    
@api_view(['POST'])
def tugasUpdate(request, pk):
    tugas = Tugas.objects.get(id=pk)
    serializer = TugasSerializer(instance=tugas, data=request.data) 

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE

@api_view(['DELETE'])
def siswaDelete(request, pk):
    siswa = Siswa.objects.get(id=pk)

    siswa.delete()

    return Response('DELETE SUCCESSFULLY')

@api_view(['DELETE'])
def tugasDelete(request, pk):
    tugas = Tugas.objects.get(id=pk)

    tugas.delete()

    return Response('DELETE SUCCESSFULLY')
