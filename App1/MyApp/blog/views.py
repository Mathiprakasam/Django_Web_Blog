from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from .models import Post, About
from django.core.paginator import Paginator
from .forms import ContactForms

# Create your views here.

#static demo data

# posts=[
#         {'id':1,'title':'VK hits Six','content':'Sports'},
#         {'id':2,'title':'School Reopening Announcement','content':'Education'},
#         {'id':3,'title':'New style Dodthis','content':'Fashion'},
#         {'id':4,'title':'Nano Science demand increases','content':'Science'},
#         {'id':5,'title':'AI tunrs into AGI','content':'Technology'},
#         {'id':6,'title':'No GST upto 12LPA salary','content':'Commerce'},
#         {'id':7,'title':'Organic producers needed','content':'Food'},
#         {'id':8,'title':'Cancer medicine introduced in Russian market','content':'Health'},
#         {'id':9,'title':'Pongal winner Madhagajaraja','content':'Entertainment'},
#         {'id':10,'title':'Next gen 39T launch','content':'Automobile'},
#     ]




def index(request):
    blog_title="ADM Posts"  
    #getting data from model
    all_posts=Post.objects.all() 

    #Paginator
    paginator=Paginator(all_posts,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)


    return render(request,'blog/index.html',{'blok_titke':blog_title,'page_obj':page_obj})

def detail(request,slug):
    
    #sample
    # post=next((item for item in posts if item['id']==post_id),None)
    

    #logger
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'Post id={post}')

    try:
        post=Post.objects.get(slug=slug)
        related_post=Post.objects.filter(category=post.category).exclude(pk=post.id)
    
    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")

    return render(request,'blog/detail.html',{"post":post,"related_post":related_post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_redirect(request):
    return HttpResponse("HI NEW URL")


def contacts(request):

    if request.method == 'POST':
        form = ContactForms(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        logger=logging.getLogger("TESTING")
        if form.is_valid():
            # form.cleaned_data['name']
            # print("Form is valid")
            
            logger.debug(f"POST {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_msg="Your Email has been sent"
            return render(request,'blog/contacts.html',{'form':form,"success_msg":success_msg})

        else:
            print(f"Not valid form reason is {form.errors}")
            logger.debug(f'Form submission failure{form.errors}')
        
        return render(request,'blog/contacts.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'blog/contacts.html')



def about(request):
    about_content=About.objects.first().content
    return render(request,"blog/about.html",{"about_content":about_content})

    