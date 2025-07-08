from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import get_object_or_404


def index(request):
    """
    Render the index page for the contact app.
    """
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[0:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contacts - ',
    }
    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    """
    Render the single contact page for the contact app.
    """
    # single_contact = Contact.objects.get(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
