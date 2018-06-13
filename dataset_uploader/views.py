import datetime
import re
from django.shortcuts import render
from dataset_uploader.models import Submission
from marketplace.models import Posting, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from . import forms


@login_required
def index(request):
    if request.method == 'POST':
        increase_by = request.POST.get('increase-by') or 1
        name = request.POST.get('name')
        no_of_entries = int(request.POST.get('no-entries'))
        date_of_submission = datetime.datetime

        user = User.objects.filter(id=request.user.id).get()
        profile = user.userprofileinfo

        submission = Submission(user_profile=profile, data_type="Image", no_of_entries=no_of_entries, name=name,
                                date_of_submission=date_of_submission, increase_by=increase_by)

        submission.save()

        return HttpResponseRedirect('/submissions/')

    submissions = Submission.objects.order_by('no_of_entries')
    my_dict = {'submissions': submissions}

    return render(request, 'dataset_uploader/index.html', context=my_dict)


@login_required
def my_submissions(request):
    if request.method == 'PATCH':
        print(request.body)
        data_as_str = request.body.decode('utf-8').replace('+', ' ')
        regex = re.match('^edit-submission-id=(\d+)&name=(.+)$', data_as_str)
        id = regex.group(1)
        new_name = regex.group(2)

        submission = Submission.objects.get(pk=id)
        submission.name = new_name
        submission.save()

        return HttpResponse(status=200)
    elif request.method == 'POST':
        price = request.POST.get('price')
        category_id = request.POST.get('category-id')
        category = Category.objects.filter(id=category_id).first()

        submission_id = request.POST.get('submission_id')
        sub = Submission.objects.filter(id=submission_id).get()
        post = Posting(submission=sub, price=price, user=request.user.userprofileinfo)
        post.save()

        sub.posting = post
        sub.save()

        category.postings.add(post)

        return HttpResponseRedirect('/submissions/')
    elif request.method == 'DELETE':
        body_str = request.body.decode('utf-8')
        id = re.match('^id=(\d+)$', body_str).group(1)

        Submission.objects.get(pk=id).delete()

        return HttpResponse(status=200)

    profile = request.user.userprofileinfo
    submissions = profile.submission_set.all()
    no_of_submissions = len(submissions)
    categories = Category.objects.all()

    return render(request, 'dataset_uploader/submissions.html',
                  {'submissions': submissions, 'no_of_submissions': no_of_submissions, 'categories': categories})


@login_required
def new_submission(request):
    form = forms.DataSubmission()

    if request.method == 'POST':
        form = forms.DataSubmission(request.POST)

        if form.is_valid():
            print("Validation Success")

            print('name: ' + form.cleaned_data['name'])

    return render(request, 'dataset_uploader/submission_form.html', {'form': form})
