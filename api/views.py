from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.

class HomeView(View):
  def get(self,request):
    return JsonResponse(
      {"message": "Yahhh it's working............."}
    )
    
class TestView(View):
  def get(self , request):
    return JsonResponse({
      "message": "this is a second route."
    })
