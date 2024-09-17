from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
import random
from .models import Participant
from .forms import ParticipantForm


def is_it_christmas_today(request):
    today = date.today()
    is_christmas = today.month == 12 and today.day == 25
    return render(request, "christmas.html", {"is_it_christmas": is_christmas})


def game(request):
    participants = Participant.objects.all()
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("game")
    else:
        form = ParticipantForm()

    if "generate_pairs" in request.POST:
        pairs = generate_santa_pairs(participants)
        return render(request, "pairs.html", {"pairs": pairs})

    return render(
        request,
        "secret_santa.html",
        {"form": form, "participants": participants},
    )


def generate_santa_pairs(participants):
    givers = list(participants)
    while True:
        receivers = list(participants)
        random.shuffle(receivers)
        if all(giver != receiver for giver, receiver in zip(givers, receivers)):
            break
    pairs = list(zip(givers, receivers))
    return pairs


def delete_all_participants(request):
    if request.method == "POST":
        Participant.objects.all().delete()
        return redirect("game")
    return redirect("game")
