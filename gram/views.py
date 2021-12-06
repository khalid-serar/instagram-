from django.shortcuts import render

from .models import Image,Like

from gram.forms import NewPostForm, SignupForm, UserProfileForm, UserUpdateForm
from django.http import request
from .email import send_welcome_email
from django.http import Http404,HttpResponseRedirect

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image, Profile
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    profile = Profile.objects.all()
    posts = Image.objects.all()

    return render(request,'home.html',{"profile":profile, "posts":posts})


#Sign up Function
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def user_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=request.user)
        # user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            user_form.save(commit=False)
            profile_form.save()
            return redirect('profile')
    else: 
        profile_form = UserProfileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile_edit.html', {"user_form":user_form,"profile_form": profile_form})

# @login_required(login_url='/accounts/login/')
# def newPost(request):
#     current_user = request.user
    
#     if request.method == 'POST':
#         form = NewPostForm(request.POST, request.FILES)        
#         if form.is_valid():
#             image=form.cleaned_data.get('image')
#             image_caption=form.cleaned_data.get('image_caption')
#             image = Image(image = image,image_caption= image_caption)
#             image.save_image()
            
#         else:
#             print(form.errors)

#         return redirect('home')

#     else:
#         form = NewPostForm()
#     return render(request, 'newPost.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    profile= Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = request.user.profile
            image.save()
            return redirect("home")
    else:
        form = NewPostForm()
    return render (request, 'newPost.html', {"form":form})    

def search_profile(request): 
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        search_results = Profile.search_profile(name)
        message = f'name'
        parameters = {
            'results': search_results,
            'message': message
        }
        return render(request, 'search.html', parameters)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})

def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Like.objects.get_or_create(liker=current_user, image=image)
    new_like.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])