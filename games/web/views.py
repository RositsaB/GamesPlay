from django.shortcuts import render, redirect

from games.web.forms import CreateProfileForm, CreateGameForm, EditProfileForm, DeleteProfileForm, EditGameForm, \
    DeleteGameForm
from games.web.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
        }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    games = Game.objects.all()
    avg_rating = sum([game.rating for game in games]) / len(games)
    context = {
        'profile': profile,
        'games': games,
        'avg_rating': avg_rating,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Game.objects.all().delete()
        return redirect('home')
    else:
        form = DeleteProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


def game_create(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()
    context = {
        'form': form,
        'profile': profile,
        }
    return render(request, 'create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)
    context = {
        'game': game,
        'form': form,
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'game': game,
        'form': form,
    }
    return render(request, 'delete-game.html', context)
