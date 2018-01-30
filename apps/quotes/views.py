from django.shortcuts import render, redirect
from .models import *
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    quotes = Quote.objects.exclude(quote_favorites__user__id=request.session['user_id'])
    favorites = Favorite.objects.filter(user_id=request.session['user_id'])
    context={
        'quotes':quotes,
        'favorites': favorites
    }
    return render(request, 'quotes/home.html', context)

def add_to_list(request, id):
    Favorite.objects.create(quote_id=id, user_id=request.session['user_id'])
    return redirect(reverse('quotes:home'))

def add_quote(request):
    if len(request.POST['author']) < 5:
        messages.warning(request, "**Quoted By field must be at least 5 characters.**")
        return redirect(reverse('quotes:home'))
    if len(request.POST['message']) < 10:
        messages.warning(request, "**Message must be 10 characters or more.**")
        return redirect(reverse('quotes:home'))
    Quote.objects.create(author = request.POST['author'], message = request.POST['message'], posted_by_id=request.session['user_id'])
    return redirect(reverse('quotes:home'))

def remove(request, id):
    user=User.objects.get(id=request.session['user_id'])
    user.user_favorites.filter(quote_id=id).delete()
    return redirect(reverse('quotes:home'))

def user(request, id):
    user = User.objects.get(id=id)
    quotes = user.user_posts.all()
    total = len(quotes)
    context={
        'user':user,
        'quotes': quotes,
        'total':total
    }

    return render(request, 'quotes/user_quotes.html', context)
