import re
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from marketplace.models import Category, Posting, Status
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    categories = Category.objects.all()
    postings = Posting.objects.all()
    no_of_entries_after_scaling = {}

    for posting in postings:
        scaling_factor = int(re.match('(\d+)X?', posting.submission.increase_by).group(1))
        after_scaling = posting.submission.no_of_entries * scaling_factor

        no_of_entries_after_scaling[posting.id] = after_scaling

    return render(request, 'marketplace/index.html',
                  {'categories': categories, 'no_of_postings': len(postings), 'postings': postings, 'no_of_entries': no_of_entries_after_scaling})


def post_description(request):
    return render(request, 'marketplace/post_description.html')


def user_profile(request, **kwargs):
    if request.method == 'POST':
        status_body = request.POST.get('status-body')
        Status.objects.create(body=status_body, user_profile=request.user.userprofileinfo)

        return HttpResponse(status=200)

    username = kwargs['username']
    user = User.objects.filter(username=username).first()
    profile = user.userprofileinfo

    postings = profile.posting_set.all()
    no_of_postings = len(postings)

    statuses = profile.statuses.all()
    no_of_statuses = len(statuses)

    # my_username = request.

    context = {'username': username, 'about': profile.about, 'postings': postings, 'no_of_postings': no_of_postings,
               'statuses': statuses, 'no_of_statuses': no_of_statuses}
    return render(request, 'marketplace/user_profile.html', context)


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
                return render(request, 'login.html', {'error': 'Account not active'})
        else:
            return render(request, 'login.html', {'error': 'Invalid username/password'})
    else:
        return render(request, 'login.html', {})


def posts_of_category(request, **kwargs):
    requested_category = kwargs['category'].title()
    print('category: ' + requested_category)
    all_categories = Category.objects.all()
    category_obj = Category.objects.filter(name=requested_category).first()
    postings = category_obj.postings.all()

    no_of_entries_after_scaling = {}

    for posting in postings:
        scaling_factor = int(re.match('(\d+)X?', posting.submission.increase_by).group(1))
        after_scaling = posting.submission.no_of_entries * scaling_factor

        no_of_entries_after_scaling[posting.id] = after_scaling

    print(len(postings))
    context = {'categories': all_categories, 'category': requested_category, 'postings': postings,
               'no_of_postings': len(postings), 'no_of_entries': no_of_entries_after_scaling}
    return render(request, 'marketplace/index.html', context)
