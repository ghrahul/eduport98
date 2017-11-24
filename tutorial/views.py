from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from .models import Subject,Note
class IndexView(generic.ListView):
    template_name = 'tutorial/index.html'
    context_object_name = 'all_subject'
    def get_queryset(self):
        return Subject.objects.all()

class DetailView(generic.DetailView):
    model = Subject
    template_name = 'tutorial/details.html'

class SubjectCreate(CreateView):
    model = Subject
    fields = ['tutor','subject_name','subject_area']

class NoteCreate(CreateView):
    model = Note
    fields = ['note_subject','note_title','note_drive']

class SubjectUpdate(UpdateView):
    model = Subject
    fields = ['tutor','subject_name','subject_area']

class SubjectDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('tutorial:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'tutorial/registration_form.html'
    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # clean normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('tutorial:index')
        return render(request,self.template_name,{'form': form})

        



