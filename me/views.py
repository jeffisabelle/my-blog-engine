from django.shortcuts import render_to_response


def me(request):
    return render_to_response('me/me.html')


def schedule(request):
    return render_to_response('me/schedule.html')
