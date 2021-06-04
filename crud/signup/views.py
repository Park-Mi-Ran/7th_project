from django.shortcuts import redirect, render, get_object_or_404
from .models import Signup
from django.utils import timezone
# Create your views here.

def home(request):
    signup = Signup.objects.all()
    return render(request,'home.html',{'signup':signup})

def detail(request, id):
    detail = get_object_or_404(Signup, pk = id)
    return render(request, 'detail.html', {'detail':detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_member = Signup()
    new_member.name = request.POST['name']
    new_member.age = request.POST['age']
    new_member.email = request.POST['email']
    new_member.introduce = request.POST['introduce']
    new_member.pub_date = timezone.now()
    new_member.save()
    return redirect('detail', new_member.id)

def edit(request,id):
    edit_member = Signup.objects.get(id=id)
    return render(request,'edit.html', {'member':edit_member})

def update(request,id):
    update_member = Signup.objects.get(id=id)
    update_member.name = request.POST['name']
    update_member.age = request.POST['age']
    update_member.email = request.POST['email']
    update_member.introduce = request.POST['introduce']
    update_member.pub_date = timezone.now()
    update_member.save()
    return redirect('detail', update_member.id)

def delete(request,id):
    delete_member = Signup.objects.get(id=id)
    delete_member.delete()
    return redirect('home')
