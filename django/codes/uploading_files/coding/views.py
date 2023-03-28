from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os

from UploadingFiles.settings import BASE_DIR


# views for html pages
def index(request):
    return render(request, 'index.html', {})


def any_file(request):
    return render(request, 'any_file.html', {})


def message(request):
    message = request.session.get('message')
    return render(request, 'message.html', {'message': message})


def multiple_files(request):
    return render(request, 'multiple_files.html', {})


def particular_file(request):
    return render(request, 'particular_file.html', {})


def sized_file(request):
    return render(request, 'sized_file.html', {})


def ajax_file(request):
    return render(request, 'ajax_file.html', {})


def ajax_multiple_files(request):
    return render(request, 'ajax_multiple_files.html', {})


def view_ajax_files(request):
    return render(request, 'view_ajax_files.html', {})


# views for receiving and uploading files
def upload_any_file(request):
    file = request.FILES['any_file']
    if not file:
        request.session['message'] = 'no file is selected'
        return redirect('/message')

    # If folder is not available then it will be created automatically
    fs = FileSystemStorage(location='uploads/all_formats')
    file = fs.save(file.name, file)  # returns name of saved file
    if file:
        request.session['message'] = 'File is uploaded successfully'
    else:
        request.session['message'] = 'Something went wrong. Try later'

    return redirect('/message')


def upload_multiple_files(request):
    files = request.FILES.getlist('files')
    if not files:
        request.session['message'] = 'no file(s) is selected'
        return redirect('/message')

    fs = FileSystemStorage(location='uploads/multiple_files')

    token = 0
    for file in files:
        if fs.save(file.name, file):  # returns name of saved file
            continue
        else:
            token = 1
            break

    if token == 0:
        request.session['message'] = 'Files are uploaded successfully'
    else:
        request.session['message'] = 'Something went wrong. Try later'

    return redirect('/message')


def upload_specific_size_file(request):
    file = request.FILES['file']
    if not file:
        request.session['message'] = 'no file is selected'
        return redirect('/message')

    fs = FileSystemStorage(location='uploads/ParticularSizeFiles')
    file = fs.save(file.name, file)  # returns name of saved file
    if file:
        request.session['message'] = 'File is uploaded successfully'
    else:
        request.session['message'] = 'Something went wrong. Try later'

    return redirect('/message')


def upload_particular_format_file(request):
    file = request.FILES['pic_file']
    if not file:
        request.session['message'] = 'no file is selected'
        return redirect('/message')

    file_extension_check = file.name.endswith('.jpeg') or file.name.endswith('.jpg') or file.name.endswith('.png')
    if file_extension_check:
        fs = FileSystemStorage(location='uploads/particular_formats')
        file = fs.save(file.name, file)  # returns name of saved file
        if file:
            request.session['message'] = 'File is uploaded successfully'
        else:
            request.session['message'] = 'Something went wrong. Try later'

        return redirect('/message')
    else:
        request.session['message'] = 'Only image files are allowed with .jpeg, .jpg and .png extensions'
        return redirect('/message')


def upload_ajax_file(request):
    file = request.FILES.get('ajax_file')
    if not file:
        return HttpResponse('no file is selected')
    else:
        fs = FileSystemStorage(location='uploads/AjaxFiles')
        file = fs.save(file.name, file)  # returns name of saved file
        if file:
            return HttpResponse('File is uploaded successfully')
        else:
            return HttpResponse('Something went wrong. Try later')


def upload_ajax_multiple_files(request):
    files = request.FILES.getlist('files')
    if not files:
        return HttpResponse('no file is selected')
    else:
        fs = FileSystemStorage(location='uploads/AjaxMultipleFiles')

        token = 0
        for file in files:
            if fs.save(file.name, file):  # returns name of saved file
                continue
            else:
                token = 1
                break

        if token == 0:
            return HttpResponse('Files are uploaded successfully')
        else:
            return HttpResponse('Something went wrong. Try later')


# view for listing, deleting and downloading uploaded files
def view_files(request, type):
    if type == 'all_formats':
        path = os.path.join(BASE_DIR, 'uploads\\all_formats')
        files_dict = make_files_dict(path)
    elif type == 'multiple_files':
        path = os.path.join(BASE_DIR, 'uploads\\multiple_files')
        files_dict = make_files_dict(path)
    elif type == 'specific_formats':
        path = os.path.join(BASE_DIR, 'uploads\\particular_formats')
        files_dict = make_files_dict(path)
    else:
        path = os.path.join(BASE_DIR, 'uploads\\ParticularSizeFiles')
        files_dict = make_files_dict(path)

    if files_dict:
        return render(request, 'view_files.html', {'files_dict': files_dict})
    else:
        request.session['message'] = 'no file is uploaded yet'
        return redirect('/message')


def view_ajax_files(request, type):
    if type == 'ajax_file':
        path = os.path.join(BASE_DIR, 'uploads\\AjaxFiles')
        files_dict = make_files_dict(path)
    else:
        path = os.path.join(BASE_DIR, 'uploads\\AjaxMultipleFiles')
        files_dict = make_files_dict(path)

    if files_dict:
        return render(request, 'view_ajax_files.html', {'files_dict': files_dict})
    else:
        request.session['message'] = 'no file is uploaded yet'
        return redirect('/message')


def download_file(request):
    file_path = request.GET.get('file_path')
    if os.path.isfile(file_path):
        file_name = request.GET.get('file_name')
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read())
            response['Content-Disposition'] = 'attachment;filename=' + file_name
            return response
    else:
        request.session['message'] = 'File not found....'
        return redirect('/message')


def delete_file(request):
    file_path = request.GET.get('file_path')
    if os.path.isfile(file_path):
        os.remove(file_path)
        request.session['message'] = 'File is deleted successfully'
    else:
        request.session['message'] = 'File not found....'
    return redirect('/message')


def delete_ajax_file(request):
    file_path = request.GET.get('file_path')
    if os.path.isfile(file_path):
        os.remove(file_path)
        return HttpResponse('success')
    else:
        return HttpResponse('failed')


# helper functions
def make_files_dict(path):
    files_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            files_dict[file] = os.path.join(root, file)
    return files_dict
