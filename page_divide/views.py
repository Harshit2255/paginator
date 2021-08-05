from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def Post_page(request):
    all_posts = Post.posts.all()
    paginator = Paginator(object_list=all_posts, per_page=3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj' : page_obj}
    return render(request, 'page_divide/home.html', context)


