# website/urls.py
from django.urls import path
from .views import (
    advocacy_awareness,
    annual_grant,
    board_of_trustees,
    contact_success,
    discretionary_grant,
    donation_success,
    donation_view,
    education_programme,
    event_list,
    health_programme,
    index,
    about,
    news_list,
    news_detail,
    contact_view,
    partnership_collaboration,
    programmes,
    projects_supported,
    publication_list,
    scholarship,
    skills_development,
    team,
    thank_you_view,
    trustee_detail,
    emergency_relief,
    video_list,
    volunteer_list,
)

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("news/", news_list, name="news_list"),
    path("news/<int:pk>/", news_detail, name="news_detail"),
    path("contact/", contact_view, name="contact"),
    path("programmes/", programmes, name="programmes"),
    path("programmes/health/", health_programme, name="health_programme"),
    path("programmes/emergency_relief/", emergency_relief, name="emergency_relief"),
    path("programmes/education/", education_programme, name="education_programme"),
    path(
        "programmes/skills_development/", skills_development, name="skills_development"
    ),
    path(
        "programmes/advocacy_awareness/", advocacy_awareness, name="advocacy_awareness"
    ),
    path("programmes/projects/", projects_supported, name="projects_supported"),
    path("board-of-trustees/", board_of_trustees, name="board_of_trustees"),
    path("trustees/<int:pk>/", trustee_detail, name="trustee_detail"),
    path("team/", team, name="team"),
    path("donate/", donation_view, name="donate"),
    path("donate/success/", donation_success, name="donation_success"),
    path("contact-us/success/", contact_success, name="contact_success"),
    path("publications/", publication_list, name="publication_list"),
    path("videos/", video_list, name="video_list"),
    path("scholarship/", scholarship, name="scholarship"),
    path("annual_grant/", annual_grant, name="annual_grant"),
    path("discretionary_grant/", discretionary_grant, name="discretionary_grant"),
    path(
        "partnership-collaboration/",
        partnership_collaboration,
        name="partnership_collaboration",
    ),
    path("thank-you/", thank_you_view, name="thank_you_page"),
    path("events/", event_list, name="event_list"),
    path("volunteers/", volunteer_list, name="volunteer_list"),
]
