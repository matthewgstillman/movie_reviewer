from django.shortcuts import render, redirect 

from .models import User, Movie

# Create your views here.
def index(request):
    return render(request, 'new_movie_reviewer/index.html')

def login(request):
    users = User.objects.all()
    postData = {
        'username': request.POST['username'],
        'password': request.POST['password']
    }
    if request.method == 'POST':
        messages = User.objects.login(request.POST)
    if not messages:
        print("Success! No Messages!")
        current_user = User.objects.all().filter(username=request.POST['username'])
        request.session['id'] = current_user.id
        request.session['first_name'] = current_user.first_name
        return redirect('/movies')
    else:
        request.session['messages'] = messages
        return redirect('/')

def register(request):
    #print request.POST    
    if request.method == 'POST':
        messages = User.objects.register(request.POST)
        #Above Line Might Be postData
    if not messages:
        print("No messages! Success")
        #Fetch User ID and name via username
        user_list = User.objects.all().filter(username=request.POST['username'])
        request.session['id'] = user_list[0].id
        request.session['first_name'] = user_list[0].first_name
        request.session['last_name'] = user_list[0].last_name
        request.session['name'] = str(request.session['first_name'] + " " + str(request.session['last_name']))
        return redirect('/reviews')

def movies(request):
    messages = []
    users = User.objects.all()
    current_user = User.objects.get(id=request.session['id'])
    print ( "Current User:" + str(current_user))
    movies = Movie.objects.all()
    # user_list = User.objects.all().filter(username=request.POST['username'])
    # request.session['id'] = user_list[0].id
    # reviewer = User.objects.get(id=request.session['id'])
    if request.method == 'GET':
        users = User.objects.all()
        current_user = User.objects.get(id=request.session['id'])
        print ( "Current User:" + str(current_user))
        movies = Movie.objects.all()
        context = {
            'current_user': current_user,
            'users': users,
            'movies': movies
        }
        return render(request, 'new_movie_reviewer/movies.html', context)
    if request.method == 'POST':
        messages = Movie.objects.create_movie(request.POST)
    if not messages:
        # first_name = request.session['first_name']
        print("No messages! Success! Creating Movie Review!")
        print("Redirect Motherfucker! Didnt see that coming, did you?")
        return render(request, 'new_movie_reviewer/movies.html')

def reviews(request):
    movies = Movie.objects.all()
    users = User.objects.all()
    current_user = User.objects.get(id=request.session['id'])
    print ("Current User: " + str(current_user))
    context = {
        'current_user': current_user,
        'movies': movies,
        'users': users
    }
    print(movies)
    return render(request, 'new_movie_reviewer/reviews.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')