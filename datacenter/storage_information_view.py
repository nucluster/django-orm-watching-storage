from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import format_duration


def storage_information_view(request):
    non_closed_visits = []
    d = {'True': 'Да!', 'False': 'Нет'}
    for item in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                "who_entered": item.passcard.owner_name,
                "entered_at": item.entered_at,
                "duration": format_duration(item.get_duration()),
                "is_strange": d[str(item.is_visit_long())]
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
