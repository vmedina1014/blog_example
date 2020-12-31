from blog import views
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^post/($<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^post/new/$', views.CreatePostView.as_view(), name='post_create'),
    re_path(r'^post/($<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^post/($<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    re_path(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?<pk>\d+/)comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'^comment/(?<pk>\d+/)approve/$',views.comment_approve,name='comment_approve'),
    re_path(r'^comment/(?<pk>\d+/)remove/$',views.comment_remove,name='comment_remove'),
    re_path(r'^post/($<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

]

