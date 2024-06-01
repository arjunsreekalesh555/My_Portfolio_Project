from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    datas=Bio.objects.all()
    project=Projects.objects.all()
    certificate=Certificates.objects.all()

    return render(request, 'admin/index.html', {'datas':datas, 'certificate':certificate, 'project':project})

def addBio(request):
    datas=Bio.objects.all()

    if request.method=='POST':
        form=bioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('view_bio')

    else:
        form=bioForm()

    return render(request, 'admin/add_bio.html', {'datas':datas, 'form':form})


def viewBio(request):
    datas=Bio.objects.all()

    return render(request, 'admin/bio.html', {'datas':datas})

def addCertificates(request):
    certis=Certificates.objects.all()

    if request.method=='POST':
        form=certificatesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('view_certificates')

    else:
        form=certificatesForm()


    return render(request, 'admin/add_certificates.html', {'certis':certis, 'form':form})

def viewCertificates(request):
    certificate=Certificates.objects.all()

    return render(request, 'admin/view_certificate.html', {'certificate': certificate})

def certificateDetails(request, certificate_id):
    certificate=Certificates.objects.get(id=certificate_id)

    return render(request, 'admin/certificate_details.html', {'certificate':certificate})


def deleteCertificate(request, certificate_id):
    certificate=Certificates.objects.get(id=certificate_id)

    if request.method=='POST':
        certificate.delete()

        return redirect('view_certificates')

    return render(request, 'admin/delete_certificate.html', {'certificate':certificate})

def addProjects(request):
    projects=Projects.objects.all()

    if request.method=='POST':
        form=projectsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('view_projects')

    else:
        form=projectsForm()


    return render(request, 'admin/add_projects.html', {'projects':projects, 'form':form})

def viewProjects(request):
    project=Projects.objects.all()

    return render(request, 'admin/view_projects.html', {'project': project})

def projectDetails(request, project_id):
    project=Projects.objects.get(id=project_id)

    return render(request, 'admin/project_details.html', {'project':project})


def deleteProject(request, project_id):
    project=Projects.objects.get(id=project_id)

    if request.method=='POST':
        project.delete()

        return redirect('view_projects')

    return render(request, 'admin/delete_project.html', {'project':project})

def updateBio(request, data_id):
    bio=get_object_or_404(Bio, id=data_id)

    if request.method=='POST':
        form=bioForm(request.POST, request.FILES, instance=bio)
        if form.is_valid():
            form.save()
            return redirect('view_bio')
    else:
        form = bioForm(instance=bio)

    return render(request, 'admin/update_bio.html', {'form': form, 'bio':bio})

def Contacts(request):

    return render(request, 'admin/contacts.html')
