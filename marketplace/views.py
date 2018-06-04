from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from marketplace.models import Category, Posting


# Create your views here.
def index(request):
    categories = Category.objects.all()
    postings = Posting.objects.all()
    return render(request, 'marketplace/index.html', {'categories': categories, 'no_of_postings': len(postings), 'postings': postings})


def post_description(request):
    return render(request, 'marketplace/post_description.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            return render(request, 'login.html', {'error': 'Invalid username/password'})
    else:
        return render(request, 'login.html', {})


def posts_of_category(request, **kwargs):
    requested_category = kwargs['category'].capitalize()
    print('category: ' + requested_category)
    all_categories = Category.objects.all()
    category_obj = Category.objects.filter(name=requested_category).first()
    postings = category_obj.postings.all()
    context = {'categories': all_categories, 'category': requested_category, 'postings': postings, 'no_of_postings': len(postings)}
    print(len(postings))
    return render(request, 'marketplace/index.html', context)
