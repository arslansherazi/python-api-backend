import os

from flask import render_template, session, redirect, request, send_file
from werkzeug.utils import secure_filename

from app import app


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# views for html pages
@app.route('/')
def index():
    return render_temp
    late('index.html')


@app.route('/any_file')
def any_file():
    return render_template('any_file.html')


@app.route('/multiple_files')
def multiple_files():
    return render_template('multiple_files.html')


@app.route('/particular_file')
def particular_file():
    return render_template('particular_file.html')


@app.route('/specific_size_file')
def specific_size_file():
    return render_template('sized_file.html')


@app.route('/ajax_file')
def ajax_file():
    return render_template('ajax_file.html')


@app.route('/ajax_multiple_files')
def ajax_multiple_files():
    return render_template('ajax_multiple_files.html')


@app.route('/message')
def message():
    message = session['message']
    return render_template('message.html', message=message)


# views for receiving and uploading files
@app.route('/upload_any_file', methods=['POST'])
def upload_any_file():
    file = request.files['any_file']
    if not file:
        session['message'] = 'no file is selected'
        return redirect('/message')
    else:
        filename = secure_filename(file.filename)
        if not os.path.exists('Uploads/AllFormats'):
            os.makedirs('Uploads/AllFormats')
        try:
            file.save(os.path.join('Uploads/AllFormats/', filename))
            session['message'] = 'File is uploaded successfully'
        except Exception as e:
            session['message'] = str(e)
        return redirect('/message')


@app.route('/upload_multiple_files', methods=['POST'])
def upload_multiple_files():
    files = request.files.getlist('files')
    if not files:
        session['message'] = 'no file(s) is selected'
        return redirect('/message')
    else:
        token = 1
        if not os.path.exists('Uploads/MultipleFiles'):
            os.makedirs('Uploads/MultipleFiles')
        for file in files:
            filename = secure_filename(file.filename)
            try:
                file.save(os.path.join('Uploads/MultipleFiles/', filename))
            except Exception as e:
                token = 0
                session['message'] = str(e)
        if token:
            session['message'] = 'Files are uploaded successfully'
        return redirect('/message')


@app.route('/upload_specific_size_file', methods=['POST'])
def upload_specific_size_file():
    file = request.files['file']
    if not file:
        session['message'] = 'no file is selected'
        return redirect('/message')
    else:
        file.seek(0, os.SEEK_END)
        file_size_in_bytes = file.tell()
        file_size_in_kbs = file_size_in_bytes / 1000
        file_size_in_mbs = file_size_in_kbs / 1000
        if file_size_in_kbs >= 10.0 and file_size_in_mbs <= 5.0:
            filename = secure_filename(file.filename)
            if not os.path.exists('Uploads/ParticularSizeFiles'):
                os.makedirs('Uploads/ParticularSizeFiles')
            try:
                file.save(os.path.join('Uploads/ParticularSizeFiles/', filename))
                session['message'] = 'File is uploaded successfully'
            except Exception as e:
                session['message'] = str(e)
            return redirect('/message')
        else:
            session['message'] = 'Please Upload file of size between 10KB-5MB'
            return redirect('/message')


@app.route('/upload_particular_format_file', methods=['POST'])
def upload_particular_format_file():
    file = request.files['pic_file']
    if not file:
        session['message'] = 'no file is selected'
        return redirect('/message')
    else:
        file_extension = file.mimetype.split('/')[1]
        allowed_extensions = ['jpeg', 'jpg', 'png']
        file_extension_check = file_extension in allowed_extensions
        if file_extension_check:
            filename = secure_filename(file.filename)
            if not os.path.exists('Uploads/ParticularFormats'):
                os.makedirs('Uploads/ParticularFormats')
            try:
                file.save(os.path.join('Uploads/ParticularFormats/', filename))
                session['message'] = 'File is uploaded successfully'
            except Exception as e:
                session['message'] = str(e)
            return redirect('/message')
        else:
            session['message'] = 'Only image files are allowed with .jpeg, .jpg and .png extensions'
            return redirect('/message')


@app.route('/upload_ajax_file', methods=['POST'])
def upload_ajax_file():
    file = request.files['ajax_file']
    if not file:
        return 'no file is selected'
    else:
        filename = secure_filename(file.filename)
        if not os.path.exists('Uploads/AjaxFiles'):
            os.makedirs('Uploads/AjaxFiles')
        try:
            file.save(os.path.join('Uploads/AjaxFiles/', filename))
            return 'File is uploaded successfully'
        except Exception as e:
            return str(e)


@app.route('/upload_ajax_multiple_files', methods=['POST'])
def upload_ajax_multiple_files():
    files = request.files.getlist('files')
    if not files:
        return 'no file(s) is selected'
    else:
        token = 1
        if not os.path.exists('Uploads/AjaxMultipleFiles'):
            os.makedirs('Uploads/AjaxMultipleFiles')
        for file in files:
            filename = secure_filename(file.filename)
            try:
                file.save(os.path.join('Uploads/AjaxMultipleFiles/', filename))
            except Exception as e:
                token = 0
                return str(e)
        if token:
            return 'Files are uploaded successfully'


# view for listing, deleting and downloading uploaded files
@app.route('/view_files/<type>')
def view_files(type):
    if type == 'all_formats':
        path = 'Uploads/AllFormats'
        files_dict = make_files_dict(path)
    elif type == 'multiple_files':
        path = 'Uploads/MultipleFiles'
        files_dict = make_files_dict(path)
    elif type == 'specific_formats':
        path = 'Uploads/ParticularFormats'
        files_dict = make_files_dict(path)
    elif type == 'ajax_file':
        path = 'Uploads/AjaxFiles'
        files_dict = make_files_dict(path)
    elif type == 'ajax_multiple_files':
        path = 'Uploads/AjaxMultipleFiles'
        files_dict = make_files_dict(path)
    else:
        path = 'Uploads/ParticularSizeFiles'
        files_dict = make_files_dict(path)

    if files_dict:
        files = {'files_dict': files_dict}
        if type == 'ajax_file' or type == 'ajax_multiple_files':
            return render_template('view_ajax_files.html', files=files)
        else:
            return render_template('view_files.html', files=files)
    else:
        session['message'] = 'no file is uploaded yet'
        return redirect('/message')


@app.route('/download_file')
def download_file():
    file_path = request.args['file_path']
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)  # as_attachment=True is used to download file with same name
    else:
        session['message'] = 'File not found....'
        return redirect('/message')


@app.route('/delete_file')
def delete_file():
    file_path = request.args['file_path']
    if os.path.isfile(file_path):
        os.remove(file_path)
        session['message'] = 'File is deleted successfully'
    else:
        session['message'] = 'File not found....'
    return redirect('/message')


@app.route('/delete_ajax_file')
def delete_ajax_file():
    file_path = request.args['file_path']
    if os.path.isfile(file_path):
        os.remove(file_path)
        return 'success'
    else:
        return 'failed'


# helper functions
def make_files_dict(path):
    files_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            files_dict[file] = os.path.join(root, file)
    return files_dict
