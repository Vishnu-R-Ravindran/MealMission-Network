from django.shortcuts import  get_object_or_404, render,redirect
from sharebite.models import *
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

# Create your views here.
def index(request):
   return render(request,"d.html")

def orp(request):
   return render(request,"o.html")

def home(request):
   return render(request,"home.html")

def coordinatorhome(request):
   return render(request,"x.html")

def hotelhome(request):
   return render(request,"n.html")

def service(request):
   return render(request,"service.html")
def adm(request):
   return render(request,"admin.html")


def contact(request):
   return render(request,"contact.html")



    
def coordinatorreg(request):
   if request.method=="POST":
      name=request.POST.get("txt")
      email=request.POST.get("email")
      number=request.POST.get("phone")
      password=request.POST.get("pswd")
      im=request.FILES.get("img")
      gender=request.POST.get("gender")
      uage=request.POST.get("ag")
      obj=coordinator(name=name,email=email,number=number,password=password,image=im,gender=gender,age=uage)
      obj.save()
   return render(request,'coordinator.html',)



def coordinatorlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = coordinator.objects.get(email=email)
            if user.password == password:  
                request.session["email"] = user.email
                return redirect("coordinatorhome")
        except coordinator.DoesNotExist:
            pass
            
    return render(request, "coordinator.html")

def coordinatorprofile(request):
   email=request.session['email']
   if email:
      
      user=coordinator.objects.get(email=email)
      return render(request,'coordinatorprofile.html',{'user':user})
   return render(request,"x.html")
def coupdate(request):
    email = request.session.get('email')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        image = request.FILES.get('image', None)

        # Get the user object or return 404 if not found
        obj = get_object_or_404(coordinator, email=email)
        
        # Update the user fields
        obj.name = name
        obj.email = email
        obj.number = number
        obj.password = password
        obj.image = image if image else obj.image  
        obj.gender = gender
        obj.age = age
        
       
        obj.save()
        
        # Prepare user information for rendering
        user_info = {
            'name': obj.name,
            'email': obj.email,
            'number': obj.number,
            'password': obj.password,
            'image': obj.image,
            'gender': obj.gender,
            'age': obj.age,
        }
        
        return render(request, 'x.html', user_info)
    else:
        # Handle non-POST requests if needed
        return HttpResponse("Invali-d request method.", status=405)
    
#hotel

def hotelreg(request):
    if request.method == "POST":
        # Fetching data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone")
        location = request.POST.get("location")
        password = request.POST.get("pswd")
        food_capacity = request.POST.get("food_capacity")
        food_type = request.POST.get("food_type")
        image = request.FILES.get("img")
        
        # Creating a new Hotel object
        try:
            hotel = Hotel(
                name=name,
                email=email,
                phone_number=phone_number,
                location=location,
                password=password,
                image=image,
                food_capacity=food_capacity,
                food_type=food_type
            )
            hotel.save()  # Saving the object to the database
            return render(request, 'hotel.html', {'message': 'Hotel registered successfully!'})
        except Exception as e:
            # Handling errors (e.g., email uniqueness constraint violation)
            return render(request, 'hotel.html', {'error': str(e)})
    
    return render(request, 'hotel.html')




def hotellogin(request):
   if request.method=="POST":        
      email=request.POST.get("email")
      password=request.POST.get("pswd") 

      try:
         us=Hotel.objects.get(email=email,password=password)
         semail=us.email
         request.session["email"]=semail
         return redirect("hotelhome")
      except:
         msg="invalid username"
         return render(request,"n.html",{"msg":msg})
   return render(request,"n.html")




def logout(request):
   request.session.flush()
   return render(request,'d.html')

def hotel_profile(request):
    if 'email' in request.session:
        # Retrieve email from session
        email = request.session['email']
        
        try:
            # Fetch the hotel using the email
            hotel = Hotel.objects.get(email=email)
            return render(request, 'hotel_profile.html', {'hotel': hotel})
        except Hotel.DoesNotExist:
            return redirect('hotel_login')  
    return redirect('hotel_login')  



def houpdate(request):
    if 'email' in request.session:  # Check if user is logged in
        email = request.session['email']
        hotel = Hotel.objects.get(email=email)

        if request.method == "POST":
            # Retrieve form inputs
            name = request.POST.get('name')
            new_email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            location = request.POST.get('location')
            food_capacity = request.POST.get('food_capacity')
            food_type = request.POST.get('food_type')
            password = request.POST.get('password')

            # Check for email conflicts if email is changed
            if new_email != email and Hotel.objects.filter(email=new_email).exists():
                alert = "<script>alert('Email already exists'); window.location.href='/hotelprofile/';</script>"
                return HttpResponse(alert)

            # Update fields
            hotel.name = name
            hotel.email = new_email
            hotel.phone_number = phone_number
            hotel.location = location
            hotel.food_capacity = food_capacity
            hotel.food_type = food_type

            # Update password if provided
            if password:
                hotel.password = password

            # Handle image upload
            if 'image' in request.FILES:
                hotel.image = request.FILES['image']

            # Save the updated information
            hotel.save()
            alert = "<script>alert('Profile updated successfully'); window.location.href='/profile_1/';</script>"
            return HttpResponse(alert)

        return render(request, 'hotel.html', {'hotel': hotel})

    alert = "<script>alert('You must log in to update your profile'); window.location.href='/hotellogin/';</script>"
    return HttpResponse(alert)



#admin

def adlogin(request):
    if request.method=='POST':
        name = request.POST.get('name')
        password = request.POST.get('pswd')
        u = 'admin'
        p = 'admin'
        if name==u:
            if password==p:
                return redirect('adm')
            else:
             return render(request,"adminlogin.html")
        else:
             return render(request,"adminlogin.html")
    else:
         return render(request,"adminlogin.html")





#hotel
def log_donation(request):
    # Fetch the currently logged-in hotel using session data
    hotel_email = request.session.get('email')
    if not hotel_email:
        alert = "<script>alert('You must be logged in to log a donation.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    hotel = get_object_or_404(Hotel, email=hotel_email)

    if request.method == "POST":
        food_details = request.POST.get('food_details', '').strip()
        quantity = request.POST.get('quantity')
        proposed_pickup_time = request.POST.get('proposed_pickup_time')
        proposed_location = request.POST.get('proposed_location', '').strip()

        # Validation checks
        if not food_details or not quantity or not proposed_pickup_time or not proposed_location:
            alert = "<script>alert('All fields are required.'); window.location.href='/donate/';</script>"
            return HttpResponse(alert)

        if not quantity.isdigit() or int(quantity) <= 0:
            alert = "<script>alert('Quantity must be a positive number.'); window.location.href='/donate/';</script>"
            return HttpResponse(alert)

       
        try:
            Donation.objects.create(
                hotel=hotel,
                food_details=food_details,
                quantity=int(quantity),
                proposed_pickup_time=proposed_pickup_time,
                proposed_location=proposed_location
            )
            alert = "<script>alert('Donation logged successfully!'); window.location.href='/listy/';</script>"
            return HttpResponse(alert)
        except Exception as e:
            alert = f"<script>alert('An error occurred: {e}'); window.location.href='/donate/';</script>"
            return HttpResponse(alert)

    return render(request, 'log_donation.html')


def view_donationss(request):
    # Check if the hotel is logged in using the session email
    hotel_email = request.session.get('email')
    if not hotel_email:
        alert = "<script>alert('You must be logged in to view donations.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch the hotel using the email from the session
    hotel = get_object_or_404(Hotel, email=hotel_email)

    # Retrieve donations logged by the hotel
    donations = Donation.objects.filter(hotel=hotel).order_by('-id')

    # If no donations are found, display an alert and redirect
    if not donations.exists():
        alert = "<script>alert('No donations found.'); window.location.href='/donate/';</script>"
        return HttpResponse(alert)

    # Render the donations view with the list of donations
    return render(request, 'view_donations.html', {'donations': donations})

def delete_donation(request, id):
    if request.method == "POST":
        # Assuming the logged-in user's email is stored in the session
        email = request.session.get('email')
        if not email:
            alert = "<script>alert('You must be logged in to delete donations.'); window.location.href='/logout/';</script>"
            return HttpResponse(alert)

        # Retrieve the donation using the id from the URL
        donation = get_object_or_404(Donation, id=id, hotel__email=email)

        try:
            # Deleting the donation
            donation.delete()
            alert = "<script>alert('Donation deleted successfully!'); window.location.href='/listy/';</script>"
            return HttpResponse(alert)
        except Exception as e:
            alert = f"<script>alert('An error occurred: {e}'); window.location.href='/listy/';</script>"
            return HttpResponse(alert)
    else:
        alert = "<script>alert('Invalid request method.'); window.location.href='/listy/';</script>"
        return HttpResponse(alert)
    



#orphanage

def orphanage_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pswd")
        try:
            orphanage = Orphanage.objects.get(email=email, password=password)
            email = orphanage.email
            request.session["email"] = email
            return redirect("o_h") 
        except Orphanage.DoesNotExist:
            alert = "<script>alert('Invalid username or password'); window.location.href='/ol/';</script>"
            return HttpResponse(alert)
    return render(request, "or_log.html")



def orphanage_register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone")
        password = request.POST.get("pswd")
        im = request.FILES.get("img")
        address = request.POST.get("address")
        capacity = request.POST.get("capacity")
        current_occupancy = request.POST.get("current_occupancy")
        orphanage_type = request.POST.get("orphanage_type")
        
        # Check if orphanage with the same email already exists
        if Orphanage.objects.filter(email=email).exists():
            alert = "<script>alert('Orphanage with this email already exists'); window.location.href='/or/';</script>"
            return HttpResponse(alert)
        
        # Create new orphanage object
        obj = Orphanage(name=name, email=email, phone_number=phone_number, password=password,
                        image=im, address=address, capacity=capacity, current_occupancy=current_occupancy,
                        orphanage_type=orphanage_type)
        obj.save()
        
        alert = "<script>alert('Registration successful! Please log in.'); window.location.href='/ol/';</script>"
        return HttpResponse(alert)
    
    return render(request, "or_log.html")


def or_pro(request):
    if 'email' in request.session:
        id = request.session['email']
        usr = Orphanage.objects.get(email=id)
        context = {
            'g': usr,
            'orphanage_types': Orphanage.ORPHANAGE_TYPE_CHOICES  # Added choices
        }
        return render(request, 'profile.html', context)
    return redirect('ol')

def edit_or_pro(request):
    if 'email' in request.session and request.method == 'POST':
        id = request.session['email']
        usr = Orphanage.objects.get(email=id)
        
        # Update fields
        usr.name = request.POST.get('name')
        usr.phone_number = request.POST.get('phone_number')
        usr.address = request.POST.get('address')
        usr.current_occupancy = request.POST.get('current_occupancy')
        usr.capacity = request.POST.get('capacity')
        usr.orphanage_type = request.POST.get('orphanage_type')
        
        # Handle image upload (if a new image is uploaded)
        if 'image' in request.FILES:
            usr.image = request.FILES['image']
        
        usr.save()
        return redirect('or_pro')  # Redirect back to profile page after update
    return redirect('ol')



def view_available_donations(request):
    # Check if the user is logged in via session
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as an orphanage to view available donations.'); window.location.href='/ol/';</script>"
        return HttpResponse(alert)

    # Fetch the logged-in orphanage
    id = request.session['email']
    try:
        usr = Orphanage.objects.get(email=id)
    except Orphanage.DoesNotExist:
        alert = "<script>alert('Invalid orphanage account. Please log in again.'); window.location.href='/ol/';</script>"
        return HttpResponse(alert)

    # Get the current date and time
    current_datetime = timezone.now()

    # Fetch donations with status 'PENDING' and proposed_pickup_time >= today
    donations = Donation.objects.filter(
        status='PENDING',
        proposed_pickup_time__gte=current_datetime
    ).order_by('-created_at')

    # Check if no donations are available
    if not donations.exists():
        alert = "<script>alert('No available donations found. Redirecting to the dashboard.'); window.location.href='/o_h/';</script>"
        return HttpResponse(alert)

    # Render available donations
    return render(request, 'available_donations.html', {'donations': donations})



def request_donation(request, donation_id):
    # Check if the user is logged in via session
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as an orphanage to request donations.'); window.location.href='/ol/';</script>"
        return HttpResponse(alert)

    # Fetch the logged-in orphanage
    id = request.session['email']
    try:
        usr = Orphanage.objects.get(email=id)
    except Orphanage.DoesNotExist:
        alert = "<script>alert('Invalid orphanage account. Please log in again.'); window.location.href='/ol/';</script>"
        return HttpResponse(alert)

    # Get the donation object
    donation = get_object_or_404(Donation, id=donation_id)

    # Check if the donation is still available
    if donation.status != 'PENDING':
        alert = "<script>alert('This donation is no longer available.'); window.location.href='/available_donations/';</script>"
        return HttpResponse(alert)

    # Update the donation's status and assign the orphanage
    donation.orphanage = usr
    donation.status = 'REQUESTED'
    donation.save()

    alert = "<script>alert('Donation requested successfully!'); window.location.href='/available_donations/';</script>"
    return HttpResponse(alert)





#admin
def view_donations(request):
    donations = Donation.objects.filter(status='REQUESTED')

    if not donations:
        alert = "<script>alert('No requests yet.'); window.location.href='/adm/';</script>"
        return HttpResponse(alert)
    
    return render(request, 'admin_dashboard.html', {'donation': donations})


def approve_and_assign_coordinator(request, donation_id):
 
    donation = get_object_or_404(Donation, id=donation_id)

    if donation.status != 'REQUESTED':
        alert = "<script>alert('Only requested donations can be approved.'); window.location.href='/adm/';</script>"
        return HttpResponse(alert)

    if request.method == "POST":
     
        coordinator_email = request.POST.get('coordinator_email')
        try:
            assigned_coordinator = coordinator.objects.get(email=coordinator_email)
        except coordinator.DoesNotExist:
            alert = "<script>alert('Invalid coordinator email.'); window.location.href='/adhome/';</script>"
            return HttpResponse(alert)

        # Assign coordinator and approve donation
        donation.coordinator = assigned_coordinator
        donation.status = 'APPROVED'
        donation.save()

        alert = "<script>alert('Donation approved and coordinator assigned!'); window.location.href='/adm/';</script>"
        return HttpResponse(alert)

    # Render a form to select coordinator (for GET request)
    coordinators = coordinator.objects.all()
    return render(request, 'assign_coordinator.html', {'donation': donation, 'coordinators': coordinators})



def reject_donation(request, donation_id):
    # Fetch the donation
    donation = get_object_or_404(Donation, id=donation_id)

    # Ensure the donation is in 'REQUESTED' status
    if donation.status != 'REQUESTED':
        alert = "<script>alert('Only requested donations can be rejected.'); window.location.href='/adhome/';</script>"
        return HttpResponse(alert)

    # Clear orphanage and set status to 'PENDING'
    donation.orphanage = None
    donation.status = 'PENDING'
    donation.save()

    alert = "<script>alert('Donation has been rejected and set to pending.'); window.location.href='/adm/';</script>"
    return HttpResponse(alert)


#coordinator


def view_assigned_donations(request):
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as a coordinator.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    coordinator_email = request.session['email']
    # Fetch the coordinator object
    try:
        coordinators = coordinator.objects.get(email=coordinator_email)
    except coordinator.DoesNotExist:
        alert = "<script>alert('Coordinator not found.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch donations assigned to this coordinator and status 'APPROVED'
    donations = Donation.objects.filter(coordinator=coordinators, status='APPROVED').order_by('-created_at')
    if not donations.exists():
        alert = "<script>alert('No assigned works  found for you.'); window.location.href='/coordinatorhome/';</script>"
        return HttpResponse(alert)


    return render(request, 'coordinator_dashboard.html', {'donations': donations})




def mark_as_collected(request, donation_id):
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as a coordinator.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    coordinator_email = request.session['email']
    try:
        coordinators = coordinator.objects.get(email=coordinator_email)
    except coordinator.DoesNotExist:
        alert = "<script>alert('Coordinator not found.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch the donation assigned to this coordinator
    donation = get_object_or_404(Donation, id=donation_id, coordinator=coordinators)

    # Ensure donation is in 'APPROVED' status
    if donation.status != 'APPROVED':
        alert = "<script>alert('Donation is not in approved status.'); window.location.href='/coordinator_dashboard/';</script>"
        return HttpResponse(alert)

    # Update status to 'COLLECTED'
    donation.status = 'COLLECTED'
    donation.save()

    alert = "<script>alert('Donation marked as collected.'); window.location.href='/coordinator_dashboard/';</script>"
    return HttpResponse(alert)

def reject(request, donation_id):
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as a coordinator.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    coordinator_email = request.session['email']
    try:
        coordinators = coordinator.objects.get(email=coordinator_email)
    except coordinator.DoesNotExist:
        alert = "<script>alert('Coordinator not found.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch the donation assigned to this coordinator
    donation = get_object_or_404(Donation, id=donation_id, coordinator=coordinators)

    # Ensure donation is in 'APPROVED' status
    if donation.status != 'APPROVED':
        alert = "<script>alert('Donation is not in approved status.'); window.location.href='/coordinator_dashboard/';</script>"
        return HttpResponse(alert)

    # Update status to 'REQUESTED'
    donation.status = 'REQUESTED'
    donation.save()

    alert = "<script>alert('Donation marked as requested.'); window.location.href='/coordinator_dashboard/';</script>"
    return HttpResponse(alert)











def view_collected_donations(request):
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as an orphanage.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    orphanage_email = request.session['email']
    
    try:
        orphanage = Orphanage.objects.get(email=orphanage_email)
    except Orphanage.DoesNotExist:
        alert = "<script>alert('Orphanage not found.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch donations assigned to this orphanage with status 'COLLECTED'
    donations = Donation.objects.filter(orphanage=orphanage, status='COLLECTED').order_by('-created_at')
    if not donations.exists():
        alert = "<script>alert('available donations are received .'); window.location.href='/o_h/';</script>"
        return HttpResponse(alert)


    return render(request, 'orphanage_dashboard.html', {'donations': donations})



def mark_as_received(request, donation_id):
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as an orphanage.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    orphanage_email = request.session['email']
    
    try:
        orphanage = Orphanage.objects.get(email=orphanage_email)
    except Orphanage.DoesNotExist:
        alert = "<script>alert('Orphanage not found.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch the donation assigned to this orphanage
    donation = get_object_or_404(Donation, id=donation_id, orphanage=orphanage)

    # Ensure the donation is in 'COLLECTED' status
    if donation.status != 'COLLECTED':
        alert = "<script>alert('Donation is not in collected status.'); window.location.href='/orphanage_dashboard/';</script>"
        return HttpResponse(alert)

    # Update status to 'RECEIVED'
    donation.status = 'RECEIVED'
    donation.save()

    alert = "<script>alert('Donation marked as received.'); window.location.href='/orphanage_dashboard/';</script>"
    return HttpResponse(alert)





def list(request):
    user=Orphanage.objects.all()
    return render(request,'list.html',{'user':user})


def delete_orphanage(request,id):
    data=Orphanage.objects.filter(id=id)
    data.delete()
    return redirect('list')



def list2(request):
    user=Hotel.objects.all()
    return render(request,'list2.html',{'user':user})

def delete_hotel(request,id):
    data=Hotel.objects.filter(id=id)
    data.delete()
    return redirect('list2')

def list_1(request):
    user=coordinator.objects.all()
    return render(request,'list3.html',{'user':user})

def delete_co(request,id):
    data=coordinator.objects.filter(id=id)
    data.delete()
    return redirect('list_1')

def listx(request):
    user = Donation.objects.filter(status='PENDING')
    return render(request,'list4.html',{'user':user}) 

def delete_d(request, id):
    user = Donation.objects.filter(id=id, status='PENDING')
    user.delete()
    return redirect('listx')



def view_coordinator_donations(request):
    # Check if the coordinator is logged in via session
    if 'email' not in request.session:
        alert = "<script>alert('You must be logged in as a coordinator to view your donations.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    email = request.session['email']
    try:
        coordinators = coordinator.objects.get(email=email)
    except coordinators.DoesNotExist:
        alert = "<script>alert('Invalid coordinator account. Please log in again.'); window.location.href='/logout/';</script>"
        return HttpResponse(alert)

    # Fetch donations where the coordinator is assigned and status is either 'COLLECTED' or 'RECEIVED'
    donations = Donation.objects.filter(coordinator=coordinators, status__in=['COLLECTED', 'RECEIVED']).order_by('-created_at')


    if not donations.exists():
        alert = "<script>alert('No donations found for you.'); window.location.href='/coordinatorhome/';</script>"
        return HttpResponse(alert)

    
    return render(request, 'coordinator_donations.html', {'donations': donations})



def submit_feedback(request):
    session_email = request.session.get('email')  

    try:
        orphanage = Orphanage.objects.get(email=session_email)  
    except Orphanage.DoesNotExist:
        alert = "<script>alert('Orphanage not found!'); window.location.href='/dashboard/';</script>"
        return HttpResponse(alert)
    if request.method == "POST":
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        Feedback.objects.create(orphanage=orphanage, message=message, rating=rating)

        alert = "<script>alert('Feedback submitted successfully!'); window.location.href='/submit_feedback/';</script>"
        return HttpResponse(alert)
    feedbacks = Feedback.objects.filter(orphanage=orphanage)

    return render(request, 'feedback.html', {'feedbacks': feedbacks})

def f_list(request):
    user=Feedback.objects.all()
    return render(request,'f.html',{'user':user})

def delete_feedback(request,id):
    data=Feedback.objects.filter(id=id)
    data.delete()
    return redirect('f_list')





# views.py
from django.core.mail import send_mail
from django.utils import timezone
from django.shortcuts import render
from datetime import timedelta
import uuid
import threading
import time


# Temporary storage for reset tokens (shared across all models)
reset_tokens = {}

def delete_token_after_delay(token):
    """Delete token after 1 minute"""
    time.sleep(60)
    if token in reset_tokens:
        del reset_tokens[token]

def forgot_password(request, model, prefix):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = model.objects.get(email=email)
            
            # Generate new token
            token = str(uuid.uuid4())
            reset_tokens[token] = {
                'email': email,
                'expiry': timezone.now() + timedelta(minutes=1),
                'model': model.__name__  # Store model name to identify later
            }
            
            # Generate reset link
            reset_link = f"http://{request.get_host()}/{prefix}-reset-password/{token}/"
            
            # Send email
            subject = f'{prefix.capitalize()} Password Reset Request'
            message = f'Click this link to reset your {prefix} password: {reset_link}\nThis link will expire in 1 minute.'
            from_email = 'project.campus4@gmail.com'
            recipient_list = [email]
            
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            
            # Start thread to delete token after 1 minute
            threading.Thread(target=delete_token_after_delay, args=(token,), daemon=True).start()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Password reset link has been sent to your email. It will expire in 1 minute.'
            })
            
        except model.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Email not found in our system.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'An error occurred: {str(e)}'
            })
    elif request.method == 'GET':
        return render(request, f'{prefix}_forgot_password.html')
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    })

def reset_password(request, token, prefix):
    
    model_map = {
        'coordinator': coordinator,
        'Hotel': Hotel,
        'Orphanage': Orphanage
    }

    if request.method == 'GET':
        if token in reset_tokens and reset_tokens[token]['expiry'] > timezone.now():
            return render(request, f'{prefix}_reset_password.html', {'token': token})
        return HttpResponse('This reset link has expired or is invalid.', status=400)
    
    if request.method == 'POST':
        if token not in reset_tokens or reset_tokens[token]['expiry'] <= timezone.now():
            return JsonResponse({
                'status': 'error',
                'message': 'This reset link has expired or is invalid.'
            })
        
        new_password = request.POST.get('new_password')
        email = reset_tokens[token]['email']
        model_name = reset_tokens[token]['model']
        model = model_map[model_name]
        
        try:
            user = model.objects.get(email=email)
            user.password = new_password  # In production, use password hashing
            user.save()
            
            # Clean up the token
            del reset_tokens[token]
            
            return JsonResponse({
                'status': 'success',
                'message': 'Password has been reset successfully.'
            })
        except model.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'User not found.'
            })
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    })

# Specific views for each model
def coordinator_forgot_password(request):
    return forgot_password(request, coordinator, 'coordinator')

def hotel_forgot_password(request):
    return forgot_password(request, Hotel, 'hotel')

def orphanage_forgot_password(request):
    return forgot_password(request, Orphanage, 'orphanage')

def coordinator_reset_password(request, token):
    return reset_password(request, token, 'coordinator')

def hotel_reset_password(request, token):
    return reset_password(request, token, 'hotel')

def orphanage_reset_password(request, token):
    return reset_password(request, token, 'orphanage')