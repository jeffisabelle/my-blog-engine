from django.shortcuts import render_to_response


def archive_generic(request):
    """

    Arguments:
    - `request`:

    """
    return render_to_response('archive/archive.html')
