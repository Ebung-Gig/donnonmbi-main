# website/urls.py
from django.urls import path
from .views import (
    board_of_trustees,
    education_programme,
    health_programme,
    index,
    about,
    news_list,
    news_detail,
    contact_view,
    programmes,
    projects_supported,
    team,
    trustee_detail,
)

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("news/", news_list, name="news_list"),
    path("news/<int:pk>/", news_detail, name="news_detail"),
    path("contact/", contact_view, name="contact"),
    path("programmes/", programmes, name="programmes"),
    path("programmes/health/", health_programme, name="health_programme"),
    path("programmes/education/", education_programme, name="education_programme"),
    path("programmes/projects/", projects_supported, name="projects_supported"),
    path("board-of-trustees/", board_of_trustees, name="board_of_trustees"),
    path("trustees/<int:pk>/", trustee_detail, name="trustee_detail"),
    path("team/", team, name="team"),
]
