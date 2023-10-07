from django.urls import path

from questions.views import (question_create_view, question_detail_view, question_list_view, question_search_view,
                             question_update_view, question_delete_view, question_upvote_view, question_downvote_view,
                             answer_create_view, answer_update_view, answer_delete_view, answer_upvote_view,
                             answer_downvote_view, tag_list_view, tag_create_view)

app_name = 'questions'
urlpatterns = [
    path('create/', question_create_view, name='question_create'),
    path('detail/<int:question_id>/', question_detail_view, name='question_detail'),
    path('update/<int:question_id>/', question_update_view, name='question_update'),
    path('delete/<int:question_id>/', question_delete_view, name='question_delete'),
    path('upvote/<int:question_id>/', question_upvote_view, name='question_upvote'),
    path('downvote/<int:question_id>/', question_downvote_view, name='question_downvote'),
    path('answer/create/<int:question_id>/', answer_create_view, name='answer_create'),
    path('answer/update/<int:answer_id>/', answer_update_view, name='answer_update'),
    path('answer/delete/<int:answer_id>/', answer_delete_view, name='answer_delete'),
    path('answer/upvote/<int:answer_id>/', answer_upvote_view, name='answer_upvote'),
    path('answer/downvote/<int:answer_id>/', answer_downvote_view, name='answer_downvote'),
    path('list/', question_list_view, name='question_list'),
    path('search/', question_search_view, name='question_search'),
    path('tags/', tag_list_view, name='tag_list'),
    path('tags/create/', tag_create_view, name='tag_create'),
]
