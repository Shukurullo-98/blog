from django.shortcuts import render, redirect

# Create your views here.
from comments.models import Comment
from .forma import CommentUser
from accounts.models import CustomUser


#
# def comment_user (request,username):
#     user=CustomUser.objects.get(username=username)
#     form=CommentUser(request.POST or None)
#     if request.method == "POST":
#         form = CommentUser(request.POST or None)
#         form.save()
#         return redirect('user_Profile' ,request.user.username)
#     context={
#         'form':form,
#         'user':user
#     }
#     return redirect('index',context)
