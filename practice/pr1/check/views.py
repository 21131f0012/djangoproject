from django.shortcuts import render,get_object_or_404
from .models import Person,Product
from django.http import HttpResponse

def home(request):

    if request.method == "POST":
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        obj = Person(name=name,mobile=mobile)
        obj.save()

    return render(request,'home.html')
def edit(request):
    persons = Person.objects.all()
    
    for person in persons:
        flag=False
        oldname = person.name
        oldmobile = person.mobile
        if request.method == "POST":
            if oldname!=None:
                newname = request.POST["name"]
                if newname!=oldname:
                    flag=True
                    oldname = newname
            if oldmobile!=None:
                newmobile = request.POST["mobile"]
                if newmobile!=oldmobile:
                    flag=True
                    oldmobile = newmobile
            if flag:    
                # obj = Person(name=oldname,mobile=oldmobile)
                # obj.save()
                person.name = oldname
                person.mobile = oldmobile

    return render(request,'edit.html',{'persons':persons})

def display(request):
    persons = Person.objects.all()
    return render(request,'display.html',{'All':persons})


def process_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity_ordered = request.POST['quantity']

    # Update the product quantity
    product.quantity -= int(quantity_ordered)
    product.save()

    return HttpResponse("Order processed successfully.")
