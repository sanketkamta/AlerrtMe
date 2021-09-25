#Login to Mongo Atlas using fascinatemeok@gmail.com

from django.shortcuts import render
from pymongo import MongoClient

def homepage(request):
    return render(request, "index.html")

def thankyou(request):
    cluster = "mongodb+srv://sanket:xieViGwln0QF117U@cluster0.2webm.mongodb.net/AlerrtMeDB?retryWrites=true&w=majority"
    client = MongoClient(cluster)
    print("Connection created!!")
    db = client.AlerrtMeDB
    alertdata = db.alertdata
    name = request.POST["name"]
    age = request.POST["age"]
    email = request.POST["email"]
    url = request.POST["url"]
    threshold = request.POST["threshold"]
    inputdata = {"name":name, "age":age, "email":email, "url":url, "threshold":threshold}
    alertdata.insert_one(inputdata)
    print("Data inserted!!")
    return render(request, "index.html")