from django.shortcuts import render, redirect
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from contact.forma import ContactForm
from .models import Posts
from comments.forma import CommentUser
from comments.models import Comment
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    post = Posts.objects.all().order_by('-date')
    if 'search' in request.GET:
        search = request.GET['search']
        post = post.filter(Q(title__icontains=search) | Q(text__icontains=search))
    else:
        post = Posts.objects.all()
    paginations = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginations.get_page(page)

    context = {
        'post': post,
        'pagination': paginations
    }
    return render(request, 'mainapp/index.html', context)


def post(request, pk):
    posts = Posts.objects.get(id=pk, status=True)
    hit_count = HitCount.objects.get_for_object(posts)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    
    comment = posts.comment.filter(parent__isnull=True)
    comment_form = CommentUser(request.POST)
    if request.method == "POST":
        comment_form = CommentUser(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            obj = comment_form.save(commit=False)
            author = request.user
            posts = posts
            obj.author = author
            obj.post = posts
            obj.save()
            return redirect('post', posts.id)
    else:
        comment_form = CommentUser()

    pos = Posts.objects.all().order_by('-date')
    context = {
        'post': posts,
        'pos': pos,
        'comment_form': comment_form,
        'comment': comment
    }
    return render(request, 'mainapp/post.html', context)


def about(request):
    return render(request, 'mainapp/about.html')


def contac(request):
    form = ContactForm(request.POST)
    print(1)
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(11)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj = obj.save()
            form.save()
            return redirect(request, 'contac')

    return render(request, 'mainapp/contact.html')
