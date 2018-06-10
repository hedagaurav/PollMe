import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Poll, Choice

from .forms import PollForm, EditPollForm, ChoiceForm


# Create your views here.


@login_required
def polls_list(request):
    """
    Renders the polls_list.html template which lists
    all the currently available polls.
    """
    # The triple quited strings are treated as garbage values
    # when they are encountered while executing the code.
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)


@login_required
def poll_detail(request, poll_id):
    """Render poll_detail.html template which allows a user to vote."""
    # poll = Poll.objects.get(id=poll_id)
    poll = get_object_or_404(Poll, id=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/poll_detail.html', context)


@login_required
def poll_vote(request, poll_id):
    if request.method == 'POST':
        """ POST is a dictionary so we can use get method on it.
        Dictionary is written with parenthesis like a = ('x' : 10)"""
        poll = get_object_or_404(Poll, id=poll_id)
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = Choice.objects.get(id=choice_id)
            # we wont define poll here, we will use the argument poll_id to
            # get the id.
            # we will do it like we did to get the poll details.
            # Here question attribute points to the poll_id.
            # poll = choice.question
            choice.votes += 1
            choice.save()
        else:
            messages.error(request, 'NOTE: No choice was found.')
            # Since here we don't want to redirect to the polls result page
            # unless the vote is given.
            # we don't have the access to the context variable coz we are
            # going to the different url/(we are reversing)
            # so we use django messages to add the flash message
            return HttpResponseRedirect(reverse('polls:detail', args=(poll_id,)))
        return render(request, 'polls/poll_result.html', {'poll': poll})
        # simple way to check if link is working properly or not using
        # HttpResponse('its working').
        # we wont need the line below because we are using django messages.
        # return render(request, 'polls/poll_result.html', {'error': True})


@login_required
def new_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            new_poll = form.save(commit=False)
            new_poll.publish_date = datetime.datetime.now()
            new_poll.owner = request.user
            new_poll.save()
            new_choice1 = Choice(poll=new_poll, choice_text=form.cleaned_data['choice1']).save()
            new_choice2 = Choice(poll=new_poll, choice_text=form.cleaned_data['choice2']).save()
            messages.success(request, 'Poll and Choices Added.', extra_tags='alert alert-success')
            return redirect('polls:list')
    else:
        form = PollForm()
    context = {'form': form, }
    return render(request, 'polls/new_poll.html', context)


@login_required
def edit_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user != poll.owner:
        return redirect('/')

    if request.method == 'POST':
        form = EditPollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Poll Edited Successfully.', extra_tags='alert alert-success'
            )
            return redirect('polls:list')
    else:
        form = EditPollForm(instance=poll)

    context = {'form': form, 'poll': poll}
    return render(request, 'polls/edit_poll.html', context)


@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user != poll.owner:
        return redirect('/')
    if request.method == 'POST':
        poll.delete()
        messages.success(request, 'Poll Deleted Successfully.', extra_tags='alert alert-success')
        return redirect('polls:list')
    context = {'poll': poll}
    return render(request, 'polls/delete_poll.html', context)


@login_required
def add_choice(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user != poll.owner:
        return redirect('/')

    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            new_choice = form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            messages.success(
                request, 'New Choice Added Successfully to Poll - {}'.format(poll),
                extra_tags='alert alert-success'
            )
            return redirect('polls:list')
    else:
        form = ChoiceForm()
    context = {'form': form}
    return render(request, 'polls/add_choice.html', context)


@login_required
def edit_choice(request, choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    poll = get_object_or_404(Poll, id=choice.poll.id)

    if request.user != poll.owner:
        return redirect('/')

    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Choice Edited Successfully in Poll - {}'.format(poll),
                extra_tags='alert alert-success'
            )
            return redirect('polls:list')
    else:
        form = ChoiceForm(instance=choice)
    context = {'form': form, 'edit_mode': True, 'choice': choice}
    return render(request, 'polls/add_choice.html', context)


@login_required
def delete_choice(request, choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    poll = get_object_or_404(Poll, id=choice.poll.id)
    if request.user != poll.owner:
        return redirect('/')
    if request.method == 'POST':
        choice.delete()
        messages.success(request, 'Choice Deleted Successfully from Poll - {}'.format(poll),
                         extra_tags='alert alert-success')
        return redirect('polls:list')
    context = {'choice': choice, }
    return render(request, 'polls/delete_choice.html', context)
