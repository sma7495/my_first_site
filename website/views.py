from django.shortcuts import render
from website.forms import ContactForm

def index_view(request):
    return render( request,'website/index.html',)


def about_view(request):
    return render( request,'website/about.html',)

def contact_view(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = ContactForm()
    return render( request,'website/contact.html',{'form':form})

def elements_view(request):
    return render( request,'website/elements.html',)