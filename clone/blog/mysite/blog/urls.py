from django.urls import path
from django.conf.urls import url
from blog import views
from blog.views import(AboutView,PostListView,PostDetailView,
CreatePostView,UpdatePostView,PostDeleteView,DraftListView,
add_comment_to_post,comment_approve,comment_remove,post_publish)

urlpatterns = [
    path('',PostListView.as_view(),name="post_list"),
    path('about/',AboutView.as_view(),name="about"),
    url('post/(?P<pk>\d+)$',PostDetailView.as_view(),name="post_detail"),
    url('post/new/$',CreatePostView.as_view(),name="post_new"),
    url('post/(?P<pk>\d+)/edit/$',UpdatePostView.as_view(),name="post_edit"),
    url('post/(?P<pk>\d+)/remove/$',PostDeleteView.as_view(),name="post_remove"),
    url('drafts/',DraftListView.as_view(),name="post_draft_list"),
    url('post/(?P<pk>\d+)/comment/$',add_comment_to_post,name="add_comment_to_post"),
    url('comment/(?P<pk>\d+)/approve/$',comment_approve,name="comment_approve"),
    url('comment/(?P<pk>\d+)/remove/$',comment_remove,name="comment_remove"),
    url('post/(?P<pk>\d+)/publish/$',post_publish,name="post_publish"),
]
