from django.shortcuts import render,redirect,get_object_or_404
from AdminApp.models import TourDestination , HotelBookingModels
from django.contrib import messages
from JourneyJunction.models import ContactMessage



# Create your views here.

def index1_page(request):
    return render(request, "index1.html")
def index_page(request):
    return render(request, "index2.html")

def add_package_pag(request):
    return render(request, "add_package.html")


def add_tour_destination(request):
    if request.method == "POST":
        # Fetching fields from POST request
        name1 = request.POST.get("destination")
        location1 = request.POST.get("location")
        description1 = request.POST.get("description")
        long_description1 = request.POST.get("long_description")  # New field
        price1 = request.POST.get("price")
        duration1 = request.POST.get("duration")
        nights1 = request.POST.get('nights')

        # Fetching new activity fields
        activity1 = request.POST.get("activity1")
        activity2 = request.POST.get("activity2")
        activity3 = request.POST.get("activity3")
        activity4 = request.POST.get("activity4")
        activity5 = request.POST.get("activity5")

        image1 = request.FILES.get('image')  # Using .get() for safer file fetching

        # Create new TourDestination object with all fields
        add_destination = TourDestination(
            Name=name1,
            Location=location1,
            Description=description1,
            LongDescription=long_description1,  # New field
            Price=price1,
            Duration=duration1,
            Nights=nights1,
            Activity1=activity1,  # New field
            Activity2=activity2,  # New field
            Activity3=activity3,  # New field
            Activity4=activity4,  # New field
            Activity5=activity5,  # New field
            Image=image1
        )

        # Saving the new tour destination
        add_destination.save()

        # Success message and redirection
        messages.success(request, "Tour destination successfully created")
        return redirect('add_tour')  # Ensure this URL name exists

    # If GET request, render the form page
    return render(request, "add_package.html")





def display_package_page(request):
    packages = TourDestination.objects.all()
    return render(request, "display_package.html",{'packages': packages})

def edit_package_page(request,des_id):
    data = TourDestination.objects.get(id=des_id)
    return render(request, 'edit_packages.html', {'data': data})


def update_package_page(request,des_id):
    if request.method == "POST":
        name1 = request.POST.get("destination")
        location1 = request.POST.get("location")
        description1 = request.POST.get("description")
        price1 = request.POST.get("price")
        duration1 = request.POST.get("duration")
        image1 = request.FILES.get('image')

        # TourDestination.objects.filter(id=des_id).update(Name=name1, Location= location1, Descrition= description1, Price=price1, Duration=duration1,)
        destination = TourDestination.objects.get(id=des_id)
        destination.Name = name1
        destination.Location = location1
        destination.Description = description1
        destination.Price = price1
        destination.Duration = duration1


        if image1:
            destination.Image = image1

        destination.save()

        messages.success(request, "Successfully updated")
        return redirect(display_package_page)


def delete_package_page(request,des_id):
    x= TourDestination.objects.filter(id=des_id)
    x.delete()
    return redirect(display_package_page)


def tour_destinations_list(request):
    # Fetch all tour destinations from the database
    tour_destinations = TourDestination.objects.all()
    return render(request, 'tour_destinations.html', {'tour_destinations': tour_destinations})


def add_hotel_packages_page(request):
    return render(request, "add_hotels.html")

def add_hotels_list(request):
    if request.method == "POST":
        hotel_name = request.POST.get('HotelName')
        hotel_rating = request.POST.get('HotelRating')
        hotel_price = request.POST.get('HotelPrice')
        hotel_location = request.POST.get('HotelLocation')
        hotel_description = request.POST.get('HotelDescription')
        hotel_link = request.POST.get('HotelLink')
        hotel_image = request.FILES.get('HotelImage')
        add_hotels = HotelBookingModels(HotelName=hotel_name, HotelRating=hotel_rating, HotelPrice=hotel_price, HotelLocation=hotel_location, HotelDescription=hotel_description, HotelImage=hotel_image, HotelLink=hotel_link)
        add_hotels.save()
        messages.success(request, "sucessfully saved the data ")
        return redirect(add_hotel_packages_page)


def display_hotel_page(request):
    data = HotelBookingModels.objects.all()
    return render(request, "display_hotels.html", {"data":data})



# def update_hotels_list(request, hot_id):
#     if request.method == "POST":
#         hotel_name = request.POST.get('HotelName')
#         hotel_rating = request.POST.get('HotelRating')
#         hotel_price = request.POST.get('HotelPrice')
#         hotel_location = request.POST.get('HotelLocation')
#         hotel_description = request.POST.get('HotelDescription')
#         hotel_link = request.POST.get('HotelLink')
#         hotel_image = request.FILES.get('HotelImage')
#         # add_hotels = HotelBookingModels(HotelName=hotel_name, HotelRating=hotel_rating, HotelPrice=hotel_price, HotelLocation=hotel_location, HotelDescription=hotel_description, HotelImage=hotel_image, HotelLink=hotel_link)
#         # add_hotels.save()
#         add_hotels = HotelBookingModels.objects.get(id=hot_id)
#         add_hotels.HotelName = hotel_name
#         add_hotels.HotelRating = hotel_rating
#         add_hotels.HotelPrice = hotel_price
#         add_hotels.HotelLocation = hotel_location
#         add_hotels.HotelDescription = hotel_description
#         add_hotels.HotelImage = hotel_image
#         add_hotels.HotelLink = hotel_link
#         add_hotels.save()
#
#         messages.success(request, "sucessfully saved the data ")
#         return redirect(display_hotel_page)



def update_hotels_list(request, hot_id):
    # Retrieve the specific hotel object
    add_hotels = get_object_or_404(HotelBookingModels, id=hot_id)

    if request.method == "POST":
        # Update the fields based on the form submission
        hotel_name = request.POST.get('HotelName')
        hotel_rating = request.POST.get('HotelRating')
        hotel_price = request.POST.get('HotelPrice')
        hotel_location = request.POST.get('HotelLocation')
        hotel_description = request.POST.get('HotelDescription')
        hotel_link = request.POST.get('HotelLink')
        hotel_image = request.FILES.get('HotelImage')

        # Update the hotel object with the new data
        add_hotels.HotelName = hotel_name
        add_hotels.HotelRating = hotel_rating
        add_hotels.HotelPrice = hotel_price
        add_hotels.HotelLocation = hotel_location
        add_hotels.HotelDescription = hotel_description
        if hotel_image:
            add_hotels.HotelImage = hotel_image  # Only update the image if a new one is provided
        add_hotels.HotelLink = hotel_link
        add_hotels.save()

        messages.success(request, "Successfully updated the hotel data.")
        return redirect('display_hotel_page')  # Redirect to the display page after updating

    # If it's a GET request, render the form with the existing hotel data
    return render(request, "update_hotel.html", {"hotel": add_hotels})


def delete_hotel_list(request,hot_id):
    x = HotelBookingModels.objects.filter(id=hot_id)
    x.delete()
    return redirect(display_hotel_page)


def view_contact_messages(request):
    # Retrieve all ContactMessage records
    contact_messages = ContactMessage.objects.all()

    return render(request, 'view_message.html', {'contact_messages': contact_messages})





