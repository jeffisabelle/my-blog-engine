# Create your views here.
from wp.models import Post, Category
from django.shortcuts import render_to_response


def show_posts(request, category="all"):
    categories = Category.objects.all()

    posts = Post.objects.filter(post_type="post", post_status="publish")
    popular_posts = posts.order_by("-post_views")[:10]
    posts = posts.order_by("-post_date")

    recents = posts[:10]

    if category is not "all":
        c = categories.filter(category_title=category)
        posts = posts.filter(post_category=c)

    posts = posts[:4]

    for p in posts:
        p.post_content = p.post_content[:900] + \
                         p.post_content[900:].split("<br")[0]

    return render_to_response('wp/posts.html', {"posts": posts,
                                                "recents": recents,
                                                "populars": popular_posts,
                                                "categories": categories})


def single_post(request, postname):
    categories = Category.objects.all()

    post = Post.objects.get(post_type="post",
                                  post_status="publish", post_name=postname)

    post.post_views += 1
    post.save()

    posts = Post.objects.filter(post_type="post", post_status="publish")
    popular_posts = posts.order_by("-post_views")[:10]
    posts = posts.order_by("-post_date")

    recents = posts[:10]

    return render_to_response('wp/post.html', {"post": post,
                                               "recents": recents,
                                               "populars": popular_posts,
                                               "categories": categories})
