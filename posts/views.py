from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BoardPostForm


def get_posts(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'boardposts.html
    template.
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "boardposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    A view that will return a Post object based on the 
    post's ID and render it to the 'postdetail.html' template, 
    or if the post cannot be found, returns a 404 error.
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def create_or_edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BoardPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BoardPostForm(instance=post)
    return render(request, 'boardpostform.html', {'form': form})
    
    
def upvote(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.votes += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})