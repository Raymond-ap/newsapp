from django.shortcuts import render
from django.views import generic
from .models import Entertainment, Sport, LifeStyle, Celebrities, Business, Technology, Health, BreakingNews
from contacts.models import Contact


def entertainment(request):
    entertainments = Entertainment.objects.all().order_by('date')
    sports = Sport.objects.all().order_by('date')
    lifestyles = LifeStyle.objects.all().order_by('date')
    celebrities = Celebrities.objects.all()
    technologies = Technology.objects.all().order_by('date')
    business = Business.objects.all()
    healths = Health.objects.all()
    breaking_news = BreakingNews.objects.all()
    context = {
        "entertainments": entertainments,
        "sports": sports,
        "lifestyles": lifestyles,
        "celebrities": celebrities,
        "technologies": technologies,
        "business": business,
        "breaking_news": breaking_news,
        "healths": healths,
    }
    return render(request, 'index.html', context)


def allTechNews(request):
    technologies = Technology.objects.all().order_by('date')
    return render(request, 'technews.html', {"technologies": technologies})


def allHealth(request):
    healths = Health.objects.all().order_by('date')
    return render(request, 'healthnews.html', {"healths": healths})


def allEntertain(request):
    entertainments = Entertainment.objects.all().order_by('date')
    return render(request, 'entertainmentNews.html', {"entertainments": entertainments})


def allSports(request):
    sports = Sport.objects.all().order_by('date')
    return render(request, 'sportNews.html', {"sports": sports})


def allLifeSytle(request):
    lifestyles = LifeStyle.objects.all().order_by('date')
    return render(request, 'lifesyle_news.html', {"lifestyles": lifestyles})


def allCelebs(request):
    celebrities = Celebrities.objects.all().all().order_by('date')
    return render(request, 'celebs_news.html', {"celebrities": celebrities})


def getCeleb(request, name):
    celebrities = Celebrities.objects.get(title=name)
    return render(request, 'celebrity_detail.html', {"celebrities": celebrities})


def allBussiness(request):
    business = Business.objects.all().order_by('date')
    return render(request, 'all_business.html', {"business": business})


def contactUs(request):
    entertainments = Entertainment.objects.all().order_by('date')
    business = Business.objects.all()
    context = {
        "entertainments": entertainments,
        "business": business,
    }
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['useremail']
        message = request.POST['message']

        contactDetails = Contact(name=name, email=email, message=message)
        contactDetails.save()
    return render(request, 'contact.html', context)


def breakingNews(request):
    breakingnews = BreakingNews.objects.all().order_by('date')
    return render(request, 'breaking_news.html', {"breakingnews": breakingnews})


class EntertainmentDetail(generic.DetailView):
    model = Entertainment
    template_name = 'entertainment_detail.html'


class SportDetail(generic.DetailView):
    model = Sport
    template_name = 'sport_detail.html'


class LifeStyleDetail(generic.DetailView):
    model = LifeStyle
    template_name = 'lifestyle.html'


class TechnologyDetail(generic.DetailView):
    model = Technology
    template_name = 'tech_detail.html'


class HealthDetail(generic.DetailView):
    model = Health
    template_name = 'healthDetail.html'


class BusinessDetail(generic.DetailView):
    model = Business
    template_name = 'businessDetail.html'


class BreakingNewsDetail(generic.DetailView):
    model = BreakingNews
    template_name = 'breaking_news_detail.html'
