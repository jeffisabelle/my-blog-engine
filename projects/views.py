from projects.models import Project
from django.shortcuts import render_to_response


def projects(request):
    all_projects = Project.objects.all()
    last_project = all_projects[len(all_projects) - 1]

    return render_to_response('projects/projects.html',
                              {'projects': all_projects,
                               'last_project': last_project})
