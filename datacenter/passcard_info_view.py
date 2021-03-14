from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    d = {'True': 'Да!', 'False': 'Нет'}
    for visit in Visit.objects.filter(passcard=passcard.pk):
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": format_duration(visit.get_duration()),
                "is_strange": d[str(visit.is_visit_long())]
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
