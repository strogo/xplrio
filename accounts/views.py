from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile
from accounts.forms import UserProfileForm


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class WelcomeView(CreateView):
    def get(self, request):

        if UserProfile.objects.filter(user=request.user).count() == 0:
            context = {'form': UserProfileForm}
            return render(request, 'registration/welcome.html', context)

        return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))
        else:
            print("Image Upload: {}".format(request.POST['profile_pic']))

        return render(request, 'registration/welcome.html', {'form': form})
