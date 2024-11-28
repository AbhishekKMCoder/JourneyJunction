from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from JourneyJunction.models import LoginDb,ContactMessage
from AdminApp.models import TourDestination , HotelBookingModels
from razorpay import client
from .models import UserProfile
import razorpay



import json
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
import razorpay
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


def new_fun(request):
    return render(request, "new.html")

def html_pag(request):
    return render(request, "index.html")

def about_pag(request):
    return render(request, "about.html")

# def tour_pag(request):
#     destinations = TourDestination.objects.all()
#     return render(request, "tour.html",{'destinations': destinations})

def tour_pag(request):

    search_query = request.GET.get('search')  # Get the search query from the request
    if search_query:
        destinations = TourDestination.objects.filter(Name__icontains=search_query)  # Filter services based on the query
    else:
        destinations = TourDestination.objects.all()

    # Convert 'star' to a float for each destination
    for destination in destinations:
        try:
            destination.star = float(destination.star)
        except (ValueError, TypeError):
            destination.star = 0  # Default to 0 if conversion fails

    return render(request, "tour.html", {'destinations': destinations})


def hotel_pag(request):
    return render(request, "hotel.html")
def blog_pag(request):
    return render(request, "blog.html")
def contact_pag(request):
    return render(request, "contact.html")

def hotel_single_pag(request):
    return render(request, "hotel_single.html")


def hotel_single_pag(request):
    return render(request, "hotel_single.html")

def tour_single_pag(request):
    return render(request, "tour_single.html")


def Loginpage(request):
    return render(request, "login.html")


def Sign_page(request):
    return render(request, "sign.html")


def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phonenumber']

        hashed_password = make_password(password)

        user = LoginDb(
            full_name=full_name,
            username=username,
            email=email,
            password=hashed_password,
            phone_number=phone_number
        )
        user.save()
        messages.success(request, "You have signed up successfully!")
        return redirect('login')

    return render(request, 'signup.html')


def User_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')

        user = LoginDb.objects.filter(username=un).first()

        if user and check_password(pwd, user.password):
            request.session['username'] = un  # Store username in session
            next_url = request.GET.get('next', 'index')  # Default to 'index' if no next URL
            return redirect(next_url)  # Redirect to the next page or index
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')



def User_logout(request):
    request.session.flush()
    messages.success(request, "You have successfully logged out.")
    return redirect('login')




# def Single_tour_detail(request,tour_id):
#     tour = TourDestination.objects.get(id=tour_id)
#     return render(request,'tour_single.html', {
#         'tour': tour
#
#     })

def Single_tour_detail(request, tour_id):
    tour = TourDestination.objects.get(id=tour_id)

    # Convert the star rating to a numeric value (float)
    try:
        tour.star = float(tour.star)
    except (ValueError, TypeError):
        tour.star = 0  # Default to 0 if conversion fails

    return render(request, 'tour_single.html', {'tour': tour})


def single_hotel_detail(request, hotel_id):
    # hotel = get_object_or_404(HotelBookingModels, id=hotel_id)
    hotel = HotelBookingModels.objects.get(id=hotel_id)
    return render(request, 'hotel_single.html', {
        'hotel': hotel
    })



def booking_form(request):
    return render(request, 'booking_form.html')

def payment_page(request):
    customer = TourDestination.objects.order_by('-id').first()

    payy = customer.Price  # Assuming this retrieves the price in INR
    amount = int(float(customer.Price) * 100)  # Convert to paise
    print(payy)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_vMHnnDmKFRgRmn', 'jhjAlUJQFVTQWX1AVUBxaB0v'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})

        order_id = customer['id']

        # Pass the `payment` object for POST requests
        return render(request, 'payment.html', {
            'customer': customer,
            'amount': amount,
            'payment': payment
        })

    # For GET requests, don't pass the `payment` object
    return render(request, 'payment.html', {
        'customer': customer,
        'amount': amount
    })

def save_user_profile(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('Name')
        location = request.POST.get('location')
        email = request.POST.get('email')

        user_profile = UserProfile(name=name, location=location, email=email)
        user_profile.save()


        return redirect(payment_page)

def contact_save(request):
    if request.method == 'POST':
        # Manually retrieve the form data from request.POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact_message.save()  # Save to the database
        messages.success(request, "Your message has been sent successfully!")

        return redirect(contact_pag)


