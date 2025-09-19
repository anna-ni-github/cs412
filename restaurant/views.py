from django.shortcuts import render
from django.utils import timezone
import random
import datetime

# Ramen restaurant menu
MENU_ITEMS = {
    "Shoyu Ramen": 14.50,
    "Tonkotsu Ramen": 15.75,
    "Miso Ramen": 13.99,
    "Gyoza (6 pcs)": 6.50,
}

def main(request):
    return render(request, "restaurant/main.html")

def order(request):
    specials = [
        "Spicy Tantanmen",
        "Black Garlic Ramen",
        "Curry Ramen",
        "Cold Hiyashi Chuka"
    ]
    daily_special = random.choice(specials)

    context = {
        "menu": MENU_ITEMS,
        "daily_special": daily_special,
    }
    return render(request, "restaurant/order.html", context)

def confirmation(request):
    if request.method == "POST":
        ordered_items = []
        total = 0

        # Collect ordered items
        for item, price in MENU_ITEMS.items():
            if request.POST.get(item):
                ordered_items.append(item)
                total += price

        # Daily special
        special_item = request.POST.get("daily_special")
        if special_item:
            ordered_items.append(special_item)
            total += 16.50  # flat price for daily special ramen

        # Customer info
        customer_name = request.POST.get("name")
        customer_phone = request.POST.get("phone")
        customer_email = request.POST.get("email")
        instructions = request.POST.get("instructions")

        # Ready time (random 30–60 minutes)
        minutes = random.randint(30, 60)
        ready_time = timezone.now() + datetime.timedelta(minutes=minutes)

        context = {
            "items": ordered_items,
            "total": round(total, 2),
            "name": customer_name,
            "phone": customer_phone,
            "email": customer_email,
            "instructions": instructions,
            "ready_time": ready_time.strftime("%I:%M %p"),
        }
        return render(request, "restaurant/confirmation.html", context)

    return render(request, "restaurant/order.html", {"menu": MENU_ITEMS})

