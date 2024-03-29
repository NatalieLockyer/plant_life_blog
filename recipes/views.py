from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect, Http404
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Returns all the published posts in :model:`recipe.Post`
    and displays them in a page of 6 posts.
    """
    template_name = "recipes/index.html"
    paginate_by = 6
    model = Post

    def get_queryset(self):
        """
        This is to override the original queryset to allow
        filtering by category.
        """
        queryset = super().get_queryset().annotate(
            comments_count=Count('comments', distinct=True)
        ).filter(status=1)

        """
        This is to capture the category from query parameters.
        """
        category = self.request.GET.get('category', None)

        if category is not None:
            try:
                category = int(category)
                queryset = queryset.filter(category=category)
            except ValueError:
                pass

        return queryset.order_by('category')

def post_detail(request, slug):
        """
        Display an individual :model:`recipes.Post`.

        **Context**

        ``post``
            An instance of :model:`recipes.Post`.

        **Template**

        :template:`recipe/index.html`

        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()

        if request.method == "POST":
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Your comment has been submitted and is waiting approval"
                )

        comment_form = CommentForm()

        return render(
            request,
            "recipes/post_detail.html",
            {"post": post,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form},
                )

def comment_edit(request, slug, comment_id):
        """
        Displays an individuals comment for edit
        **Context**

        ``post``
            An instance of :model:`recipes.Post`.
        ``comment``
            A single comment related to the post.
        ``comment_form``
            An instance of :form:`recipes.CommentForm`

        """
        if request.method == "POST":

            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comment = get_object_or_404(Comment, pk=comment_id)
            comment_form = CommentForm(data=request.POST, instance=comment)

            if comment_form.is_valid() and comment.author == request.user:
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.approved = False
                comment.save()
                messages.add_message
                (request,
                    messages.SUCCESS,
                    'Your comment has been updated!')
            else:
                messages.add_message
                (request,
                    messages.ERROR,
                    'There had been an error updating your comment!')

            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
        """
        Delete an individual comment.

        **Context**

        ``post``
            An instance of :model:`recipes.Post`.
        ``comment``
            A single comment related to the post.

        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment.delete()
            messages.add_message
            (request,
                messages.SUCCESS,
                'Your comment has now been deleted!')
        else:
            messages.add_message
            (request,
                messages.ERROR,
                'Youre only able to delete your own comments!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
