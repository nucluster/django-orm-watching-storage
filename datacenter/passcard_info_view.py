from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    for item in Visit.objects.filter(passcard=passcard.pk):
        this_passcard_visits.append(
            {
                "entered_at": item.entered_at,
                "duration": format_duration(item.get_duration()),
                "is_strange": item.is_visit_long(minutes=60)
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
