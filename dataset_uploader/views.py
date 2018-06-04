from django.shortcuts import render
from dataset_uploader.models import Submission
from django.contrib.auth.decorators import login_required
from . import forms
# from django.http import HttpResponse


# Create your views here.

@login_required
def index(request):
    submissions = Submission.objects.order_by('no_of_entries')
    my_dict = {'submissions': submissions}
    return render(request, 'dataset_uploader/index.html', context=my_dict)

@login_required
def new_submission(request):
    form = forms.DataSubmission()

    if request.method == 'POST':
        form = forms.DataSubmission(request.POST)

        if form.is_valid():
            print("Validation Success")

            print('name: ' + form.cleaned_data['name'])

    return render(request, 'dataset_uploader/submission_form.html', {'form': form})
