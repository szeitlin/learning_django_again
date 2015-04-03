from django.shortcuts import redirect, render
#from django.http import HttpResponse

from lists.models import Item, List

#home_page=None

def home_page(request):
   # if request.method=='POST':
   #      Item.objects.create(text=request.POST['item_text'])
   #      return redirect('/lists/the-only-list-in-the-world/')

   #items = Item.objects.all()
   #return render(request, 'home.html') #, {'items': items})


   #     return HttpResponse(request.POST['item_text'])
   #item = Item()
   #item.text=request.POST.get('item_text', '')
   #item.save()

   return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items':items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

#return HttpResponse('<html><title>To-Do lists</title></html>')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))