#Login to Mongo Atlas using fascinatemeok@gmail.com
from django.shortcuts import render, redirect
from pymongo import MongoClient

def homepage(request):
    return render(request, "index.html")

def thankyou(request):
    try:
        cluster = "mongodb+srv://sanket:0311@cluster0.ibkyza6.mongodb.net/?retryWrites=true&w=majority"

        client = MongoClient(cluster)
        db = client.AlerrtMeDB
        alertdata = db.alertdata
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        url = request.POST["url"]
        threshold = request.POST["threshold"]
        inputdata = {"name":name, "age":age, "email":email, "url":url, "threshold":threshold, "count":1}
        alertdata.insert_one(inputdata)
        return redirect('homepage')

    except Exception as e:
        print(e)
