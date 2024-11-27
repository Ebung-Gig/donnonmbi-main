from django.core.paginator import Paginator
from .models import News, Team, Trustee


from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def index(request):
    news_list = News.objects.all().order_by("-published_date")  # Get latest news
    paginator = Paginator(news_list, 6)  # Show 6 news items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "website/index.html", {"page_obj": page_obj})


def about(request):
    return render(request, "website/about.html")


def news_list(request):
    news_items = News.objects.all().order_by(
        "-published_date"
    )  # Adjust 'date' field as per your model
    paginator = Paginator(news_items, 20)  # 20 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "website/news_list.html", {"page_obj": page_obj})


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, "website/news_detail.html", {"news": news})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Send an email to the admin
            send_mail(
                f"New contact form submission from {name}",
                message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # You can also store the message or send a confirmation email to the user
            # Redirect or display success message
            return redirect(
                "contact"
            )  # Redirect to a success page or the same contact page
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})


def programmes(request):
    return render(request, "website/programmes.html")


def health_programme(request):
    return render(request, "website/health_programme.html")


def education_programme(request):
    return render(request, "website/education_programme.html")


def projects_supported(request):
    return render(request, "website/projects_supported.html")


def board_of_trustees(request):
    trustees = Trustee.objects.all()
    return render(request, "website/board_of_trustees.html", {"trustees": trustees})


def trustee_detail(request, pk):
    trustee = get_object_or_404(Trustee, pk=pk)
    return render(request, "website/trustee_detail.html", {"trustee": trustee})


def team(request):
    team_members = Team.objects.all()
    return render(request, "website/team.html", {"team_members": team_members})
