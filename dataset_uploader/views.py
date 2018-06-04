import datetime
from django.shortcuts import render
from dataset_uploader.models import Submission
from marketplace.models import Posting
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms


# from django.http import HttpResponse


# Create your views here.

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

        return HttpResponseRedirect('upload')

    submissions = Submission.objects.order_by('no_of_entries')
    my_dict = {'submissions': submissions}

    return render(request, 'dataset_uploader/index.html', context=my_dict)


@login_required
def my_submissions(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        submission_id = request.POST.get('submission_id')
        sub = Submission.objects.filter(id=submission_id).get()
        post = Posting(submission=sub, price=price, user=request.user.userprofileinfo)
        post.save()
        sub.posting = post
        sub.save()

        return HttpResponseRedirect('/submissions/')

    profile = request.user.userprofileinfo;
    submissions = profile.submission_set.all()
    no_of_submissions = len(submissions)

    return render(request, 'dataset_uploader/submissions.html',
                  {'submissions': submissions, 'no_of_submissions': no_of_submissions})


@login_required
def new_submission(request):
    form = forms.DataSubmission()

    if request.method == 'POST':
        form = forms.DataSubmission(request.POST)

        if form.is_valid():
            print("Validation Success")

            print('name: ' + form.cleaned_data['name'])

    return render(request, 'dataset_uploader/submission_form.html', {'form': form})
