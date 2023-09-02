from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
from docx2pdf import convert

def index(request):
    if (request.method == 'POST'):
        req_file = request.FILES['file']
        old_file_name = req_file.name
        fs = FileSystemStorage()

        filedata = fs.save(old_file_name,req_file)
        convert('convfiles/static/'+old_file_name)
        

        newfileroot = old_file_name.split('.')
        newfilename = newfileroot[0]+'.pdf'
        newf = open('convfiles/static/'+newfilename, 'rb')
        res = FileResponse(newf)

        return res
    return render(request, 'index.html')