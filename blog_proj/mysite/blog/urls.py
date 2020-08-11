from django.urls import path
from . import views


urlpatterns = [

    path('',views.PostListView.as_view(),name='blogpost_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='blogpost_detail'),
    path('post/post_new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',views.DrafListView.as_view(),name='blogpost_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.blogpost_publish,name='blogpost_publish'),

]
