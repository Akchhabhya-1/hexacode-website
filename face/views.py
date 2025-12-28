from django.shortcuts import render



from django.shortcuts import render

def first_view(request):
    return render(request, "index.html")  # Render the template

 