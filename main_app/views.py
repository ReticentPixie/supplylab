from django.shortcuts import render, redirect
from .models import Classroom
from django.views.generic import ListView
# ----- Authentication -----
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# ----- Authorization ----
from django.contrib.auth.decorators import login_required   # for view functions
from django.contrib.auth.mixins import LoginRequiredMixin   # for CBVs
# ----- Models & Forms-----



# ========== GENERAL Views ==========
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ========== AUTHENTICATION Views ==========
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # save user to database
            login(request, user)    # log user in
            return redirect('classroom_index')  # redirect to classroom_index page  # todo - is this where we want a newly signed up user to be redirected to?
        else:
            error_message = 'Invalid sign up - please try again.'
    form = UserCreationForm()       # reset the sign-up to a blank form if bad POST or GET request
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



# ========== CLASSROOM Views ==========
# todo - added here simply to verify authentication working - either:
# 1. keep (add an actual html template with content & update the view function)
# -- or -- 
# 2. remove & change out the LOGIN_REDIRECT_URL on settings.py to a different url

class ClassroomIndex(LoginRequiredMixin, ListView):
    model = Classroom
    template_name = 'classroom_list.html'
    



# ========== WISHLIST Views (i.e., - associate item with classroom) ==========


# ========== ITEM Views ==========



