from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import status
from .serializers import ProjectSerializer, RatingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView
from .models import Project, Rating
from .forms import CreateNewForm,RatingForm
from .permissions import IsAdminorReadOnly
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):

  model = Project
  template_name = 'projects/main.html' #template convention is <app>/<model>_<viewtype>.html
  context_object_name = 'projects'
  ordering = ['-id']

class PostDetailView(LoginRequiredMixin, DetailView):
  model = Project
  form_class = RatingForm
  template_name = 'projects/post_detail.html'
  context_object_name = 'project'

  def get_context_data(self, **kwargs):
    context = super(PostDetailView, self).get_context_data(**kwargs)
    context['rating'] = Rating.criteria_average(self, pk=self.object.pk)
    print(context)
    return context

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Project
  form_class = CreateNewForm
  template_name = 'projects/new_post.html'

  def form_valid(self, form):
    form.instance.publisher = self.request.user
    return super().form_valid(form)

class ProjectList(APIView):
  
  def get(self, request, format=None):
    all_projects = Project.objects.all()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)
  
  def post(self, request, format=None):
    serializers = ProjectSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  permission_classes = (IsAdminorReadOnly,)

def search(request):
  template = 'projects/search.html'
  query = request.GET.get('q') 
  results = Project.objects.filter( Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__icontains=query))  
  context ={
    'results':results,
    'term':query
  }
  return render(request, template, context)

def rate_project(request, pk):
  project = Project.get_project(pk)
  
  if request.method == 'POST':
    form = RatingForm(request.POST)
    if form.is_valid():
      rating = form.save(commit=False)
      rating.user = request.user
      rating.project = project
      rating.average = rating.user_average_rating()
      rating.save()
      return redirect('post-detail', pk = project.id)
  else:
    form = RatingForm()

  context = {'project':project,'form':form}
  return render(request,'projects/rating.html',context)

  


  
  
  









 



