from django.shortcuts import render


def index(request):
    """
    Render the contact page.
    """
    return render(
        request,
        'contact/index.html'
    )
