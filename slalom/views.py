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
    trick  = Trick.objects.get(id=trick_id)  #el truco que elijo para practicar
    progress = Done.objects.filter(owner=request.user)  # guardo todos los trucos que estan la db  "progreso"
    edit_id = 0                                         # la voy a usar dps
    
    trick_exists = False         # inicializo en false
    for pro in progress:        # hago un loop por los trucos que el usuario tiene
        if pro.trick_id == trick.id:    #chequeo si el truco ya esta  en la db "progreso"
            trick_exists = True         #si existe guardo la flag en True
            edit_id = pro.id            # gruardo el id del registro en la db "prgreso" para ese truco

    
    if request.method !='POST':     #si el usuario no envia informacion, solo carga la pagina y 
        if trick_exists:            # si el truco existe en la db "progreso",
            edit_progress = progress.get(id=edit_id)    #cargo la info que ya esta en la db "progreso"
            form = CompleteTrick(instance=edit_progress) #lo mando al formulario HTML
        else:
            form = CompleteTrick() # Si el truco no existe en la db "progreso", mando un formulario HTML vacio.
    else:
        if trick_exists == False:   #si el usuario manda request (clickea "save") y el truco no esta en la DB"progress"
            form = CompleteTrick(data=request.POST) #guardo la info del request en el formulario
            if form.is_valid():
                new_progress = form.save(commit=False)   #guardo datos para el nuevo registro en "progreso"
                new_progress.trick = trick 
                new_progress.owner = request.user
                new_progress.save()
        else:                                   #si el usuario manda request y el  truco esta en la DB  progress ,
            edit_progress = progress.get(id=edit_id)       # recupero la indo de la DB progress
            form = CompleteTrick(instance=edit_progress)     # creo formulario para HTML
            if form.is_valid:                               
                edit_progress = form.save(commit=False)     # creo una instancia del formulario para EDITARLO
                if edit_progress.complete == True:        # si "complete" esta guardada en T la paso a F
                    edit_progress.complete = False      
                else:
                    edit_progress.complete = True       # si "complete" esta en F lo paso a T 
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

    

"""
class DetailTrickView(DetailView):
    model = Trick

    def get_context_data(self,**kwargs):
        context = super(DetailTrickView, self).get_context_data(**kwargs)
        context['levels'] = Level.objects.all()
        context['dones'] = Done.objects.all()
        
        return context 
""" 



"""
class DoneCreateView(CreateView):
    model = Done
    fields = ['complete']


    def get_context_data(self,**kwargs):
        context = super(DoneCreateView, self).get_context_data(**kwargs)
        context['levels'] = Level.objects.all()
        context['tricks'] = Trick.objects.all()
        return context 

    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.trick = trick.id
        return super().form_valid(form)


"""


    




# Create your views here.
