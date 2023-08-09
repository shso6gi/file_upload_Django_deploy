import requests
import re
from django.shortcuts import render, redirect
from .models import UploadedFile
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return redirect('account:index')


@login_required
def upload_file(request):
    global get_three_values, upload_file_response_status
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            url = "https://demo.storj-ipfs.com/api/v0/add"
            files = {'file': (file.name, file.read())}
            response = requests.post(url, files=files)
            upload_file_response_status = response.status_code
            if upload_file_response_status == 200:
                get_three_values = re.findall(r'"(.*?)"', response.text)
                upload_file = UploadedFile(
                    user=request.user,
                    file_name=get_three_values[1],
                    file_hash=get_three_values[3],
                    file_size=get_three_values[5])
                upload_file.save()

            return redirect('file_upload:upload_result')

    else:
        return render(request, 'upload_file.html')


@login_required
def upload_result(request):
    if upload_file_response_status == 200:
        return render(request, 'upload_success.html', {'file_name': get_three_values[1]})
    else:
        return render(request, 'upload_fail.html')


@login_required
def mybook_list(request):
    upload_files = UploadedFile.objects.filter(user=request.user)
    # ziplist = []
    # for upload_file in upload_files:
    #     ziplist.append((upload_file.file_name, upload_file.file_hash, upload_file.file_size, upload_file.file_upload_date, upload_file.pk))
    # return render(request, 'mybook_list.html', {'ziplist': ziplist})
    return render(request, 'mybook_list.html', {'upload_files': upload_files})


@login_required
def mybook_detail(request, pk):
    try:
        upload_file = UploadedFile.objects.get(pk=pk)
    except UploadedFile.DoesNotExist:
        return render(request, 'No_PDF_Found.html')

    file_uploader = upload_file.user
    if request.user != file_uploader:
        return render(request, 'No_PDF_Found.html')
    else:
        return render(request, 'mybook_detail.html', {'upload_file': upload_file})


@login_required
def mybook_delete(request, pk):
    try:
        upload_file = UploadedFile.objects.get(pk=pk)
    except UploadedFile.DoesNotExist:
        return render(request, 'No_PDF_Found.html')

    UploadedFile.objects.get(pk=pk).delete()
    return redirect('file_upload:mybook_list')
