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

    :template:`recipe/post_detail.html`
    
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render (
        request,
        "recipes/post_detail.html",
        {"post": post},
    )



