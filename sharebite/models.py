from django.db import models
from django.shortcuts import render

# Create your models here.
    
class coordinator(models.Model):
    name=models.CharField(max_length=25,null=True,blank=True)
    email=models.EmailField(unique=True,null=True)
    number=models.IntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="userimg",null=True,blank=True)
    gender_choices=(
        ('MALE','male'),
        ('FEMALE','female')
    )
    gender=models.CharField(max_length=30,null=True,blank=True,choices=gender_choices)
    age=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name




class Hotel(models.Model):
            name = models.CharField(max_length=100)
            email = models.EmailField(unique=True)
            phone_number = models.CharField(max_length=15, null=True, blank=True)
            location = models.TextField()
            password = models.CharField(max_length=100)
            image = models.ImageField(upload_to="hotel_images", null=True, blank=True)
            food_capacity = models.PositiveIntegerField(help_text="Number of meals that can be donated per day")
            is_active = models.BooleanField(default=True)
            food_type_choices = (
                ('VEG', 'Vegetarian'),
                ('NONVEG', 'Non-Vegetarian'),
                ('BOTH', 'Both')
            )
            food_type = models.CharField(max_length=10, choices=food_type_choices, default='BOTH')
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)

            def __str__(self):
                return self.name




class Orphanage(models.Model):
    ORPHANAGE_TYPE_CHOICES = (
        ('GENERAL', 'General Orphanage'),
        ('INFANT', 'Infant Orphanage'),
        ('SPECIAL_NEEDS', 'Special Needs Orphanage'),
        ('COMMUNITY', 'Community Orphanage'),
        ('SINGLE_PARENTS', 'Single Parent Orphanage'),
        ('FOSTER', 'Foster Care Home'),
        ('ADOPTION', 'Adoption Home'),
        ('SCHOOL', 'Orphanage with Schooling'),
        ('REFUGEE', 'Refugee Orphanage'),
        ('CULTURAL', 'Cultural Orphanage'),
        ('EMERGENCY', 'Emergency Shelter Orphanage'),
    )

    name = models.CharField(max_length=100, blank=False, null=False) 
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    capacity = models.PositiveIntegerField()  
    current_occupancy = models.PositiveIntegerField()  
    orphanage_type = models.CharField(max_length=20, choices=ORPHANAGE_TYPE_CHOICES, default='GENERAL')
    image = models.ImageField(upload_to="orphanage_images", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def available_capacity(self):
        return self.capacity - self.current_occupancy



class Donation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    orphanage = models.ForeignKey(
        Orphanage, on_delete=models.SET_NULL, null=True, blank=True, 
        help_text="Orphanage assigned to this donation"
    )
    coordinator = models.ForeignKey(
       coordinator, on_delete=models.SET_NULL, null=True, blank=True, 
        help_text="Coordinator handling this donation"
    )
    food_details = models.TextField()
    quantity = models.PositiveIntegerField(help_text="Number of meals")
    proposed_pickup_time = models.DateTimeField()
    proposed_location = models.TextField()
    status_choices = (
        ('PENDING', 'Pending'),
        ('REQUESTED', 'Requested by Orphanage'),
        ('APPROVED', 'Approved by Admin'),
        ('COLLECTED', 'Collected by Coordinator'),
        ('RECEIVED', 'Received by Orphanage'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.food_details[:20]}"



def donation_status_chart(request):
    # Query donation statuses and count them
    status_data = Donation.objects.values('status').annotate(count=models.Count('status'))

    # Prepare data to pass to the template
    statuses = [item['status'] for item in status_data]
    counts = [item['count'] for item in status_data]

    return render(request, 'donation_status_chart.html', {
        'statuses': statuses,
        'counts': counts,
    })

class Feedback(models.Model):
    orphanage = models.ForeignKey(Orphanage, on_delete=models.CASCADE, related_name="feedbacks")
    message = models.TextField(max_length=1000)
    rating = models.PositiveIntegerField(default=1)  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.orphanage.name} - {self.rating}/5"
