from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.

class HomeView(View):
  def get(self,request):
    return JsonResponse(
      {"message": "Server running............."}
    )
    
class TestView(View):
  def get(self , request):
    return JsonResponse({
      "message": "this is a test route."
    })