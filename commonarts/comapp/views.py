from django.shortcuts import render
# Create your views here.
from .models import Post
from .forms import PostForm, NewUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
def mainindex(request):
    return render(request, 'comapp/mainindex.html')
def gallery(request):
    posts = Post.objects.order_by("-data")
    context = {'posts': posts}
    return render(request, 'comapp/gallery.html', context)
def send(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            new_obj = Post(
                image=form.cleaned_data['image'],
                title=form.cleaned_data['title'],
                user=User.objects.get(username=request.user.username),
                text=form.cleaned_data['text'])
            new_obj.save()
            return HttpResponseRedirect("/")
            #return render(request, 'mainindex.html', {'form': form})

    else:
        form = PostForm()

    return render(request, "comapp/post_form.html", {"form": form})
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = NewUserForm()

    return render(request, "comapp/register.html", {"form": form})

def exit(request):
    logout(request)
    return HttpResponseRedirect("/")
