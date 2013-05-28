from datetime import date

from django.shortcuts import render_to_response
from django.http import Http404
from wp.models import Category, Post


def archive_generic(request):
    """
    data returns something like
    [(u'Python', u'python', 6), (u'Programming', u'programming', 6)]
    [(title, slug, post_count), (), ()..]

    Arguments:
    - `request`:

    """

    categories = ["programming", "python", "linux", "ai", "web-dev",
                  "personal", "os"]
    arr = []

    for cate in categories:
        c = Category.objects.filter(category_slug=cate)
        if c:
            l = len(Post.objects.filter(post_category=c,
                                        post_status="publish"))

            arr.append((c[0].category_title, c[0].category_slug, l))

    data = sorted(arr, key=lambda k: k[2])[::-1]

    data_year = []

    for i in range(5):
        p = Post.objects.filter(
            post_date__range=(date(2009 + i, 1, 1), date(2010 + i, 1, 1)),
            post_status="publish"
        )

        data_year.append((2009 + i, len(p), p))

    return render_to_response('archive/archive.html', {"data_cat": data,
                                                       "data_year": data_year})


def archive_by_category(self, category):
    try:
        cat = Category.objects.filter(category_slug=category)
    except:
        raise Http404

    try:
        posts = Post.objects.filter(
            post_type="post", post_status="publish",
            post_category=cat)
        if not posts:
            raise Http404
    except:
        raise Http404

    return render_to_response("archive/archive_by_category.html",
                              {"posts": posts,
                               "cat": cat[0].category_title})


def archive_by_year(self, year):
    try:
        year = int(year)
    except:
        raise Http404

    try:
        p = Post.objects.filter(
            post_date__range=(date(year, 1, 1), date(year + 1, 1, 1)),
            post_status="publish"
        )
        if not p:
            raise Http404
    except:
        raise Http404

    return render_to_response("archive/archive_by_year.html",
                              {"posts": p,
                               "year": year})
