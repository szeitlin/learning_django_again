from django.shortcuts import redirect, render
#from django.http import HttpResponse

from lists.models import Item

#home_page=None

def home_page(request):
   if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

   items = Item.objects.all()
   return render(request, 'home.html', {'items': items})


   #     return HttpResponse(request.POST['item_text'])
   #item = Item()
   #item.text=request.POST.get('item_text', '')
   #item.save()

   return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})

    
#return HttpResponse('<html><title>To-Do lists</title></html>')

