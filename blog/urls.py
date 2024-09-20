from django.urls import path

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    UserDetailView
                    )

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "post/create/",
        PostCreateView.as_view(),
        name="post-create"
    ),
    path(
        "user/<int:pk>/detail/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
]