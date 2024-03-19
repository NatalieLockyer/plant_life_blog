from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6
 

def post_detail(request, slug):
    """
    Display an individual :model:`recipes.Post`.

    **Context**

    ``post``
        An instance of :model:`recipes.Post`.

    **Template**

    :template:`recipe/index.html`
    
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render (
        request,
        "recipes/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count
        },
    )



