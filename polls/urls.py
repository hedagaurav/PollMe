from django.urls import path

from . import views

# to add app_name= " something " then add the namespace=" something " in url of the app in root directory urls.py page
app_name = 'polls'
urlpatterns = [
    # :8000/list/ not working gives error 404 not found.
    # works with :8000/polls/list/
    path('list/', views.polls_list, name='list'),

    # to add new poll in polls list.
    path('new/', views.new_poll, name='new'),

    # to edit the existing poll in polls list. (polls/edit/1/)
    path('edit/<int:poll_id>', views.edit_poll, name='edit_poll'),

    # to delete poll
    path('delete/poll/<int:poll_id>', views.delete_poll, name='delete_poll'),

    # to add new choice
    path('edit/<int:poll_id>/choice/add/', views.add_choice, name='add_choice'),

    # to edit choice
    path('edit/choice/<int:choice_id>/', views.edit_choice, name='edit_choice'),

    # to delete a choice
    path('delete/choice/<int:choice_id>/', views.delete_choice, name='delete_choice'),

    # for polls/details/1/  note:it will give details about polls question
    path('details/<int:poll_id>/', views.poll_detail, name='detail'),

    # for form action after voting
    # polls/details/1/vote/
    path('details/<int:poll_id>/vote/', views.poll_vote, name='vote'),

]
