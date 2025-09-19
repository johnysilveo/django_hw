from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import random
from django.views import View


def sports(request):
    return render(request, "sports/main.html")
def football(request):
    return render(request, "sports/football.html")
def hokey(request):
    return render(request, "sports/hokey.html")
def basketball(request):
    return render(request, "sports/basketball.html")


def buy_tickets(request):
    if request.method != "POST":
        return redirect(reverse("sports:ticket_thanks"))

    data = {
        "sport": (request.POST.get("sport") or "").title(),
        "quantity": request.POST.get("quantity") or "1",
        "category": request.POST.get("category") or "",
        "fullname": request.POST.get("fullname") or "",
        "email": request.POST.get("email") or "",
        "phone": request.POST.get("phone") or "",
        "notes": request.POST.get("notes") or "",
    }
    request.session["last_ticket"] = data
    return redirect(reverse("sports:ticket_thanks"))

def ticket_thanks(request):
    data = request.session.pop("last_ticket", None)
    if not data:
        return HttpResponse("<div style='padding:2rem;color:#ccc;'>No ticket request found.</div>")

    html = f"""
    <div class="container py-5">
      <div class="card border-0 shadow-sm">
        <div class="card-body">
          <h1 class="h4 mb-3">Request received — thank you!</h1>
          <p class="mb-1"><strong>Sport:</strong> {escape(data['sport'])}</p>
          <p class="mb-1"><strong>Category:</strong> {escape(data['category'])}</p>
          <p class="mb-1"><strong>Quantity:</strong> {escape(data['quantity'])}</p>
          <p class="mb-1"><strong>Name:</strong> {escape(data['fullname'])}</p>
          <p class="mb-1"><strong>Email:</strong> {escape(data['email'])}</p>
          <p class="mb-1"><strong>Phone:</strong> {escape(data['phone'])}</p>
          {f"<p class='mb-1'><strong>Notes:</strong> {escape(data['notes'])}</p>" if data['notes'] else ""}
          <hr>
          <a href="/" class="btn btn-primary">Back to Home</a>
        </div>
      </div>
    </div>
    """
    return HttpResponse(html)