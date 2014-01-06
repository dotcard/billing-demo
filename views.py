from django.shortcuts import render, get_object_or_404
import glob

def main(request):
  return render(request, 'main.html')
