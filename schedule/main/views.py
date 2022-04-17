from django.shortcuts import  render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AgendaList, ListItem
from .forms import CreateNewList
# Create your views here.


def index(req):
    return render(req, "main/index.html", {})

def viewList(req):
    if req.user.is_authenticated:
        print(dir(req.user))
        print(req.user.agendalist.all ())
        print('[Logged In]')
    return render(req, "main/view_list.html", {})

def viewItem(req, id):
    ls = AgendaList.objects.get(id=id)

    if req.method == "POST":
        if req.POST.get("save"): #update the list
            for item in ls.listitem_set.all():
                if req.POST.get("c%d"%item.id) == "clicked":
                    item.done = True
                else:
                    item.done = False
                item.save()

        elif req.POST.get("newItem"): #save new item to list
            text = req.POST.get("new")
            if len(text) > 2:
                ls.listitem_set.create(text=text, done=False)
    return render(req, "main/list.html", {"agenda":ls})

def home(request):
    return render(request, "main/index.html")

def create(req):
    if not req.user.is_authenticated:
        return HttpResponseRedirect('/login')

    if req.method == "POST":
        form = CreateNewList(req.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            ls = AgendaList(name=name)
            ls.save()
            req.user.agendalist.add(ls)

        return HttpResponseRedirect('/%i'%ls.id)
    else:
        form = CreateNewList()
        return render(req, "main/create.html", {"form":form})


def deleteItem(request, list_id, txt):
    ListItem.objects.filter(text = txt).delete()
    return HttpResponseRedirect('/%i'%list_id) 


def deleteList(request, id):
    AgendaList.objects.filter(id = id).delete()
    return HttpResponseRedirect('/view') 
