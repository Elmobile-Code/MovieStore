from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()

    template_data = {'title' : 'Movies', 'movies' : movies}
    return render(request, 'movies/index.html',{'template_data': template_data})

def show(request, id):
    movie = Movie.objects.get(id=id)
    template_data = {'title' : movie.name, 'movie' : movie, 'reviews' : Review.objects.filter(movie=movie)}
    return render(request, 'movies/show.html', {'template_data': template_data})


@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()

    return redirect('movies.show', id=id)

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show', id=id)

    if request.method == 'GET':
        template_data = {'title' : 'Edit Review', 'review' : review}
        return render(request, 'movies/edit_review.html', {'template_data': template_data})

    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()

    return redirect('movies.show', id=id)

@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('movies.show', id=id)

# cart stuff
@login_required
def add_to_cart(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, movie=movie)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('movies.cart-detail')

@login_required
def remove_from_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        messages.success(request, "Item updated in your cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "The item you tried to remove does not exist in your cart.")
    return redirect('movies.cart-detail')

@login_required
def cart_detail(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'movies/cart.html', {'cart_items': items})

