from django.shortcuts import render, redirect

def home(request):
    response = redirect('/api/v1/')
    return response



