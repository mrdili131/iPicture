from django.shortcuts import render, redirect
from django.views import View
from .models import Image
from users.models import User
from .forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self,request):
        images = Image.objects.all()
        return render(request,'index.html',{"images":images})
    
class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        user = User.objects.get(id=request.user.id)
        images = Image.objects.all()
        form = UserChangeForm(instance=user)
        return render(request,'profile.html',{"form":form})
    
    def post(self,request):
        user = User.objects.get(id=request.user.id)
        images = Image.objects.all()
        form = UserChangeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,'profile.html',{"form":form})