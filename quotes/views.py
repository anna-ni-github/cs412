from django.shortcuts import render

import random

# Global lists (all from the same person)
quotes = [
    "You will face many defeats in life, but never let yourself be defeated.",
    "If you don't like something, change it. If you can't change it, change your attitude.",
    "We may encounter many defeats but we must not be defeated."
]

images = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaVBX6p1ri4zWhE8iuFmF8vVNtPKOANiG1vQ_okjqkO-xKRyE3lrw0VXuYKMiGrefNEwI&usqp=CAU",
    "https://nclhof.org/wp-content/uploads/2012/10/angelou.jpg",
    "https://bunny-wp-pullzone-a6bxrid7oy.b-cdn.net/wp-content/uploads/2022/08/AngelouMaya_f.jpg"]

def quote(request):
    selected_quote = random.choice(quotes)
    selected_image = random.choice(images)
    context = {"quote": selected_quote, "image": selected_image}
    return render(request, "quotes/quote.html", context)

def show_all(request):
    # show lists of quotes and images
    context = {"quotes": quotes, "images": images}
    return render(request, "quotes/show_all.html", context)

def about(request):
    # static info about the person and the creator
    context = {
        "person_name": "Maya Angelou",
        "bio": "Maya Angelou (1928–2014) was an American poet, memoirist, and civil rights activist.",
        "creator": "Anna Ni"
    }
    return render(request, "quotes/about.html", context)
