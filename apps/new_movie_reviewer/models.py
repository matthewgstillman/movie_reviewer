from __future__ import unicode_literals

from django.db import models
import md5
import bcrypt
import os, binascii

# Create your models here.
class UserManager(models.Manager):
    # def login(self, postData):
    #     messages = []
    #     # first_name = postData['first_name']
    #     # if len(str(first_name)) < 2:
    #     #     messages.append("First Name must be longer than 2 characters! What kind of pathetic first name is that, bruh?")
    #     # last_name = postData['last_name']
    #     # if len(str(last_name)) < 2:
    #     #     messages.append("Last Name must be longer than 2 characters! What kind of pathetic  last name is that, bruh?")
    #     username = postData['username']
    #     if len(str(username)) < 5:
    #         messages.append("Username must be longer than 5 characters, bruh!")
    #     password = postData['password']
    #     if len(str(password)) < 8:
    #         messages.append("Password must be 8 characters or longer, bruh! This shit is getting pathetic!")
    #     pw_confirm = postData['pw_confirm']
    #     if password != pw_confirm:
    #         messages.append("Passwords must match Bruh! If you're trying to be some sort of computer hacker, you're not very good at it!")
    #     if User.objects.filter(username=username):
    #         #encode the registered user's password from database to a specific format
    #         db_pw = User.objects.get(username=username).password.encode()
    #         #Compare the password with the password in database
    #         if not bcrypt.checkpw(login_pw, db_pw):
    #             messages.append("Password is Incorrect")
    #         else:
    #             messages.append("Username has already been registered!")
    #         return messages

    def login(self, postData):
        messages = []
        username = postData['username']
        password = postData['password']
        if len(str(username)) < 1:
            messages.append("Username must not be blank!")
        if len(str(username)) < 2:
            messages.append("Username must be at least 2 characters long!")
        if len(str(password)) < 1:
            messages.append("Password must not be blank")
        if len(str(password)) < 8:
            messages.append("Password must be at least 8 characters long!")
        if User.objects.filter(username=username):
            # encode the password to a specific format since the above email is registered
            login_pw = password.encode()
            # encode the registered user's password from database to a specific format
            db_pw = User.objects.get(username=username).password.encode()
            # compare the password with the password in database
            if not bcrypt.checkpw(login_pw, db_pw):
                messages.append("Password is Incorrect!")
        else:
            messages.append("Username has already been registered!")
        return messages

    def register(self, postData):
        print "register process"
        messages = []
        first_name = postData['first_name']
        if len(str(first_name)) < 1:
            messages.append("Error! First name must not be blank!")
        if len(str(first_name)) < 2:
            messages.append("Error! First name must be at least 2 characters long!")

        last_name = postData['last_name']
        if len(str(last_name)) < 1:
            messages.append("Error! Last name must not be blank!")
        if len(str(last_name)) < 2:
            messages.append("Error! Last name must be at least 2 characters long!")

        username = postData['username']
        if len(str(username)) < 2:
            messages.append("Error! Email must be at least 2 characters long!")

        password = postData['password']
        if len(str(password)) < 1:
            messages.append("Error! Password must not be blank!")
        if len(str(password)) < 8:
            messages.append("Error! Password must be at least 8 characters long!")

        pw_confirm = postData['pw_confirm']
        if pw_confirm != password:
            messages.append("Error! Passwords must match!")

        user_list = User.objects.filter(username=username)
        for user in user_list:
            print user.username
        if user_list:
            messages.append("Error! Username is already in the system!")
        if not messages:
            print "No messages"
            password = password.encode()
            salt = bcrypt.gensalt()
            hashed_pw = bcrypt.hashpw(password, salt)
            # password = password
            print "Create User"
            print hashed_pw
            User.objects.create(first_name=first_name, last_name=last_name, username=username, password=hashed_pw)
            print hashed_pw
            print User.objects.all()
            return None
        return messages

        

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pw_confirm = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", First Name: " + str(self.first_name) + ", Last Name: " + str(self.last_name) + ", Username: " + str(self.username)


class MovieManager(models.Manager):
    def login(self):
        return self

    def create_movie(self, postData):
        messages = []
        print("Adding Movie Review")
        title = postData['title']
        if len(str(title)) < 1:
            messages.append("Error! Title must not be blank!")
        if len(str(title)) < 2:
            messages.append("Error! Title must be at least 2 characters long!")
        print(title)

        year = postData['year']
        if len(str(year)) < 1:
            messages.append("Error! Year must not be blank!")
        if len(str(year)) < 2:
            messages.append("Error! Year must be at least 2 characters long!")
        print(year)

        genre = postData['genre']
        if len(str(genre)) < 1:
            messages.append("Error! Genre must not be blank!")
        if len(str(genre)) < 2:
            messages.append("Error! Genre must be at least 2 characters long!")
        print(genre)

        director = postData['director']
        if len(str(director)) < 1:
            messages.append("Error! Director must not be blank!")
        if len(str(director)) < 2:
            messages.append("Error! Director must be at least 2 characters long!")
        print(director)

        lead_role_1 = postData['lead_role_1']
        if len(str(lead_role_1)) < 1:
            messages.append("Error! Lead Role must not be blank!")
        if len(str(lead_role_1)) < 2:
            messages.append("Error! Lead Role must be at least 2 characters long!")
        print(lead_role_1)

        lead_role_2 = postData['lead_role_2']
        if len(str(lead_role_2)) < 1:
            messages.append("Error! 2nd Lead Role must not be blank!")
        if len(str(lead_role_2)) < 2:
            messages.append("Error! 2nd Lead Role must be at least 2 characters long!")
        print(lead_role_2)

        review = postData['review']
        if len(str(review)) < 1:
            messages.append("Error! Review must not be blank!")
        if len(str(review)) < 2:
            messages.append("Error! Review must be at least 2 characters long!")
        if len(str(review)) > 1500:
            messages.append("Error! You can't write a review that long!")
        print(review)


        rating = postData['rating']
        if len(str(rating)) < 1:
            messages.append("Error! Rating must not be blank!")
        print(rating)
        

        # reviewer = current_user
        # print("Reviewer: " + str(current_user))
        # if not reviewer:
        #     messages.append("Error! Must add a reviewer!")

        reviewer = postData['reviewer']
        if not reviewer:
            messages.append("Error! Review must have a reviewer!")
        print(reviewer)
        
        if not messages:
            print("No Messages!")
            Movie.objects.create(title=title, year=year, genre=genre, director=director, lead_role_1=lead_role_1, lead_role_2=lead_role_2, rating=rating, review=review, reviewer=reviewer)
            print(Movie.objects.all())
            return None
        return messages

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    lead_role_1 = models.CharField(max_length=50)
    lead_role_2 = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.TextField(max_length=1500)
    reviewer = models.ForeignKey('User', related_name="user_reviewer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()


    def __unicode__(self):
        return "id: " + str(self.id) + " Title: " + str(self.title) + ", Year: " + str(self.year) + ", Genre: " + str(self.genre) + ", Director: " + str(self.director) + ", Lead Role: " + str(self.lead_role_1) + ", Second Lead: " + str(self.lead_role_2) + ", Rating: " + str(self.rating) + ", Review: " + str(self.review) + ", Reviewer: " + str(self.reviewer)




