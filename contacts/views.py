from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(
                user_id=user_id, id=listing_id).exists()

            if has_contacted:
                messages.error(
                    request, 'You have submitted a inquiries for this listing.')
                return redirect('/listings/'+listing_id)

        contact = Contact(user_id=user_id, listing=listing,
                          listing_id=listing_id, name=name, phone=phone, email=email, message=message)
        contact.save()
        # send_mail(
        #     'Test mail',
        #     'This is a testing email.',
        #     'bagasys3@gmail.com',
        #     ['theswiesiung@gmail.com'],
        #     fail_silently=False,
        # )
        messages.success(
            request, 'Your message has been submitted, a realtor will get back to you soon.')
        return redirect('/listings/'+listing_id)
