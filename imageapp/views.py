from django.shortcuts import render
def show_image(request):
    return render(request, 'image.html')
