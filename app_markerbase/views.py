from django.shortcuts import render, redirect, get_object_or_404
from .models import Marker
from .forms import MarkerUploadForm, MarkerEditForm
from django.http import HttpResponse

def index(request):
    return render(request, 'app_markerbase/index.html')
    ##return HttpResponse("Hello, you're at the index.")

def marker_upload(request):
    if request.method == 'POST':
        form = MarkerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            marker = form.save()  # execute save() to trigger info extraction
            return redirect('marker_edit', pk=marker.pk)
    else:
        form = MarkerUploadForm()
    return render(request, 'app_markerbase/marker_upload.html', {'form': form})

def marker_edit(request, pk):
    marker = get_object_or_404(Marker, pk=pk)
    if request.method == 'POST':
        form = MarkerEditForm(request.POST, instance=marker)
        if form.is_valid():
            form.save()  # this time without renewed info extraction
            return redirect('marker_detail', pk=marker.pk)  # or list
    else:
        form = MarkerEditForm(instance=marker)
    return render(request, 'app_markerbase/marker_edit.html', {'form': form, 'marker': marker})

def marker_detail(request, pk):
    marker = get_object_or_404(Marker, pk=pk)
    return render(request, 'app_markerbase/marker_detail.html', {'marker': marker})

