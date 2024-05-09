from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from unidashboard.models import UniDetail
from .models import Company, ContactForm, History, Mission, CEO, Product
from django.http import JsonResponse
from .models import UserPost
from django.http import HttpRequest

def index(request):
    if request.user.is_authenticated:
        university = UniDetail.objects.all()
        posts = UserPost.objects.all()
        context = {
            'university': university,
            'posts': posts,
        }
        return render(request, 'index.html', context)
    else: 
        return render(request, 'video.html')

def add_post(request):
    # Handle POST request to add a new post
    if request.method == 'POST':
        content = request.POST.get('postContent')
        if content and request.user.is_authenticated:
            UserPost.objects.create(user=request.user, content=content)
            return redirect('index')  # Redirect to the index page after adding the post
        else:
            return redirect('login')  # Redirect to the login page if the user is not authenticated
    else:
        return redirect('error')  # Redirect to an error page if the request method is not POST

def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(UserPost, pk=post_id)
        if request.user.is_authenticated:
            if request.user in post.post_likes.all():
                post.post_likes.remove(request.user)
                liked = False
            else:
                post.post_likes.add(request.user)
                liked = True
            return JsonResponse({'liked': liked, 'likeCount': post.post_likes.count()})
        else:
            return JsonResponse({'error': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)




def chat_detail_view(request, id):
    university = get_object_or_404(UniDetail, pk=id)
    return render(request, 'chat.html', {'u': university})

def about(request):
    comapny = Company.objects.all()
    history = History.objects.all()
    mission = Mission.objects.all()
    ceo = CEO.objects.all()
    product = Product.objects.all()
    context = {
        'company': comapny,
        'history': history,
        'mission': mission,
        'ceo': ceo,
        'product': product,
    }
    return render(request, 'about.html', context)

def contactform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        user_query = ContactForm(name=name, email=email, message=message)
        user_query.save()
        return redirect('about')  # Redirect to the about page or any other appropriate page
    else:
        return about(request)


def search(request):
    query = request.GET.get('q')  # Retrieve the search query from the request
    
    if query:  # Check if the query is not empty
        # Split the query into individual words
        query_words = query.split()
        
        # Initialize an empty queryset to store combined search results
        combined_results = UniDetail.objects.none()
        
        for word in query_words:
            # Perform the search operation for each word using case-insensitive contains
            # Here, we use Q objects to combine multiple conditions with OR operator
            results = UniDetail.objects.filter(Q(name__icontains=word))
            
            # Combine the search results using union
            combined_results = combined_results.union(results)
        
        count = combined_results.count()  # Get the count of combined search results
    else:
        combined_results = []  # If query is empty, return an empty list
        count = 0  # Set the count to zero
    
    context = {
        'query': query,   # Pass the query to the template to display
        'results': combined_results,  # Pass the combined search results to the template
        'count': count,  # Pass the count to the template
    }
    return render(request, 'search.html', context)

