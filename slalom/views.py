from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import * 


"""
def index(request):
    levels = Level.objects.all()
    context = {'levels': levels}
    return render(request, 'slalom/index.html', context)

     
    return render(request, 'slalom/index.html')
""" 
@login_required
def trick_detail(request, trick_id):
    trick  = Trick.objects.get(id=trick_id)  
    progress = Done.objects.filter(owner=request.user)  
    edit_id = 0                                         
    
    trick_exists = False         
    for pro in progress:        
        if pro.trick_id == trick.id:    
            trick_exists = True         
            edit_id = pro.id            

    
    if request.method !='POST':     
        if trick_exists:            
            edit_progress = progress.get(id=edit_id)    
            form = CompleteTrick(instance=edit_progress) 
        else:
            form = CompleteTrick() 
    else:
        if trick_exists == False:   
            form = CompleteTrick(data=request.POST) 
            if form.is_valid():
                new_progress = form.save(commit=False)   
                new_progress.trick = trick 
                new_progress.owner = request.user
                new_progress.save()
        else:                                   
            edit_progress = progress.get(id=edit_id)       
            form = CompleteTrick(instance=edit_progress)     
            if form.is_valid:                               
                edit_progress = form.save(commit=False)     
                if edit_progress.complete == True:        
                    edit_progress.complete = False      
                else:
                    edit_progress.complete = True       
                edit_progress.save()  
                form = CompleteTrick(instance=edit_progress)
            return redirect('slalom:progress')


    context ={'trick':trick, 'form':form, 'progress': progress}
    return render(request, 'slalom/trick_detail.html', context)




class LevelListView(ListView):
    model = Level 
    template_name = 'slalom/index.html'
    context_object_name = 'levels'

@login_required
def search(request):
    search = request.GET['searched']
    tricks = Trick.objects.filter(name__icontains=search)
    context = {'tricks': tricks, 'search':search}
    return render(request, 'slalom/search-tricks.html', context)



class DetailLevelView(DetailView):
    model = Level 

    def get_context_data(self,**kwargs):
        context = super(DetailLevelView, self).get_context_data(**kwargs)
        context['tricks'] = Trick.objects.all()
        
        return context 

class ListProgressView(ListView):
    model = Done
    template_name = 'slalom/progress.html'
    def get_context_data(self,**kwargs):
        context = super(ListProgressView, self).get_context_data(**kwargs)
        context['tricks'] = Trick.objects.all()
        context['levels'] = Level.objects.all()
        return context 

class TricksListView(ListView):
    model = Trick
    template_name = 'slalom/tricks.html'
    #context_object_name = 'tricks_all'
    def get_context_data(self,**kwargs):
        context = super(TricksListView, self).get_context_data(**kwargs)
        context['done'] = Done.objects.all()
        context['levels'] = Level.objects.all()
        
        return context 





# Create your views here.
