from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrations
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.

# This function would add add the details and show them


class UserAddShowView(TemplateView):
    template_name='enroll/addandshow.html'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm=StudentRegistrations()
        stud=User.objects.all()
        context={'stu':stud,'form':fm}
        return context

    def post(self,request):
        fm=StudentRegistrations(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')
        

    

# def add_show(request):
#     if request.method == "POST":
#         fm=StudentRegistrations(request.POST)
#         if fm.is_valid():
#             nm=fm.cleaned_data['name']
#             em=fm.cleaned_data['email']
#             pw=fm.cleaned_data['password']
#             reg=User(name=nm,email=em,password=pw)
#             reg.save()
#             fm=StudentRegistrations()
        

#     else:
#         fm=StudentRegistrations()
#     stud=User.objects.all()

#     return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


# this function will delete the data



class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        del_id=(kwargs['id'])
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)

# def delete_data(request,id):
#     if request.method == 'POST':
#         pi=User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')


# This function will Update 0r Edit


class UserUpdateView(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistrations(instance=pi)     
        return render(request,'enroll/updatestudent.html',{'form':fm})

    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistrations(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
        
        






# def update_data(request,id):
#     if request.method=='POST':
       
#     else:
        