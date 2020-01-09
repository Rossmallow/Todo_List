from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TaskItem

# Create your views here.


def viewAll(request):
    all_items = TaskItem.objects.all()
    template = loader.get_template('viewTasks/index.html')
    context = {
        'all_items': all_items,
    }
    return HttpResponse(template.render(context, request))


# Create new Task Items
def addTask(request):
    new_item = TaskItem(
        title=request.POST.get('title'),
        comment=request.POST.get('comment'),
        due_date=request.POST.get('due_date'),
        star=True if request.POST.get('star') == 'on' else False
    )
    new_item.save()
    return HttpResponseRedirect('/')
