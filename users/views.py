from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .serializers import ProfileSerializer
from projects.permissions import IsAdminorReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# authentication
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# views
from django.views.generic import DetailView

# models
from django.contrib.auth.models import User
from .models import Profile


def register(request):
  if request.method == 'POST':
    # we create a form that has the request.post data
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for { username}')
      return redirect('login')

  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your account has been updated!')
      return redirect('profile')

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form': u_form,
    'p_form': p_form
  }

  return render(request, 'users/profile.html', context)




class ProfileList(APIView):
    permission_classes = (IsAdminorReadOnly,)

    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(
            all_profile, many=True, context={'request': request})
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
