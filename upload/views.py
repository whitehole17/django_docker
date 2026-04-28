from django.shortcuts import render, redirect
from .models import UploadImageForm, UploadedImage

# Create your views here.
def image_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    form = UploadImageForm()
    return render(request, 'upload/image_upload.html', {'form': form})

def upload_success(request):
    images = UploadedImage.objects.all()
    return render(request, 'upload/upload_success.html', {'images': images})