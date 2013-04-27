from projects.models import Project
from django.shortcuts import render_to_response


def projects(request):
    all_projects = Project.objects.all()
    print all_projects

    return render_to_response('projects/projects.html',
                              {'projects': all_projects})
