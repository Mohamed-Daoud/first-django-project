from django.shortcuts import render, redirect
# import a form to use Django built-in forms (i.e. Django classes)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout # to make user login & out

# Create your views here.

def signup_view(request):
    if request.method == 'POST': # POST request (i.e. button pressed) vs. GET
        signupForm = UserCreationForm(request.POST) # validate the form
        if signupForm.is_valid(): # True; form is valid
            # log the user in
            user = signupForm.save()  # save user to DB
            login(request, user)
            return redirect('articles:list')
    else: # page loaded; no data posted
        # create new instance of empty Django form
        signupForm = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':signupForm})

def login_view(request):
    if request.method == 'POST': # form filled and need to take action
        loginForm = AuthenticationForm(data=request.POST)
        if loginForm.is_valid():
            # log the user in
            user = loginForm.get_user()
            login(request, user) # the function we have imported up there
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else: # GET request, empty form loaded
        loginForm = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': loginForm})

def logout_view(request):
    # only handle the POST as there is no GET (i.e. no /logout/ page to visit)
    if request.method == 'POST':
        # Django knows the user, we do not need to pass it, log current user out
        logout(request)
        return redirect('home')
