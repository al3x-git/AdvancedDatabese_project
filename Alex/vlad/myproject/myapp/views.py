from django.urls import reverse
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .forms import *
# Create your views here.
from django.contrib import messages


class HomePageView(ListView):

    template_name = 'myapp/homepage.html'
    s_form = SocialIssueForm
    queryset = SocialIssue.objects.all()
    login_form = AuthenticationForm
    sign_form = SignUpForm

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['s_form'] = self.s_form
        context['login_form'] = self.login_form
        context['sign_form'] = self.sign_form
        return context


def signup(request):

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.success(request, 'successfully sign up!!!')

                return HttpResponseRedirect(reverse('myapp:homepage'))
        else:
            form = SignUpForm()

        messages.error(request, 'Something Went wrong Try again!!!')
        return HttpResponseRedirect(reverse('myapp:homepage'))

def login_user(request):

        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user )
                messages.success(request, 'You are successfully login')
                return HttpResponseRedirect(reverse('myapp:homepage'))

        messages.error(request, 'Something Went wrong Try again')
        return HttpResponseRedirect(reverse('myapp:homepage'))

def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse('myapp:homepage'))


def sformview(request):
    if request.method == 'POST':
        s_form = SocialIssueForm(request.POST, request.FILES)
        if not request.user.username:
            messages.error(request, "kindly Login to proceed!")
            return HttpResponseRedirect(reverse('myapp:homepage'))

        if s_form.is_valid():
            s_form.save()
        return HttpResponseRedirect(reverse('myapp:homepage'))


