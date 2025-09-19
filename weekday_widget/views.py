from django.shortcuts import render
from django.utils import timezone

def today_view(request):
    days = [
        ("Понеділок",  "linear-gradient(135deg,#2b2c52,#1b2555)"),
        ("Вівторок",   "linear-gradient(135deg,#133b5c,#0d2540)"),
        ("Середа",     "linear-gradient(135deg,#114b3b,#0b3327)"),
        ("Четвер",     "linear-gradient(135deg,#5a4029,#2e1f14)"),
        ("П'ятниця",   "linear-gradient(135deg,#4d2856,#281330)"),
        ("Субота",     "linear-gradient(135deg,#3b2c2c,#231717)"),
        ("Неділя",     "linear-gradient(135deg,#213a52,#122234)"),
    ]
    idx = timezone.localdate().weekday()
    # dev preview: /weekday/?d=0..6
    d = request.GET.get("d")
    if d and d.isdigit():
        idx = max(0, min(6, int(d)))

    day_name, day_grad = days[idx]
    bg_css = f"background-image: linear-gradient(180deg, rgba(0,0,0,.24), rgba(0,0,0,.38)), {day_grad};"
    return render(request, "weekday_widget/today.html", {"day_name": day_name, "bg_css": bg_css})
