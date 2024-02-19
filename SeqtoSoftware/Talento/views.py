from django.shortcuts import render ,redirect

# # User authentication functions in django

from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout

from .models import Profile ,Contact ,JobPosting # Import the Profile model

# To display authentication messages
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,'index.html')

def UserHome(request):
    return render(request,'index_2.html')

def ContactUs(request):
    if request.method=='POST' :
        #Cname=varible_name   , cname=name_attribute value
        Cname=request.POST['cname']
        Cemail=request.POST['cemail']
        Cmobile=request.POST['cmobile']
        Cmessage=request.POST['cmessage']

        # creating the row/record in the table:Contact 
        # object.create method -to create the store the data into tables 
        # object.all()  method to reterive the data
        #record=Contact.objects.create(column_name of table = varibale_name)
        record=Contact.objects.create(name=Cname,email=Cemail,mobile=Cmobile,message=Cmessage)
        # saving the data to database
        record.save()

    else :
        return render(request,'contact.html')

    return render(request,'contact.html')

def signin(request):
    # collecting the info from the user 
    if request.method=="POST" :
        Uname=request.POST['name']
        Upassword=request.POST['password']
        # checking and login
        user= authenticate('request',username=Uname,password=Upassword)

        if user is not None :
            messages.info(request, f"You are now logged in as {Uname}.")
            login(request, user)
            return redirect("UserHome")
        else:
            messages.info(request, "User Not Found")
            return redirect('signin')

    return render(request,'signin.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['name']
        uemail = request.POST['email']
        umobile = request.POST['mobile']
        upassword = request.POST['password']
        
        if User.objects.filter(username=uname).exists():
            messages.info(request, "Username Already Exists")
            return redirect('register')
        elif User.objects.filter(email=uemail).exists():
            messages.info(request, "Email Already Exists")
            return redirect('register')
        elif Profile.objects.filter(mobile=umobile).exists():
            messages.info(request, "Mobile Number Already Exists")
            return redirect('register')
        else:
            # Create the user
            user = User.objects.create_user(username=uname, email=uemail, password=upassword)
            # Create the associated profile
            profile = Profile.objects.create(user=user, mobile=umobile)
            messages.success(request, "User Created Successfully")
            return redirect('signin')
    
    return render(request, 'register.html')


def Post_Job(request):

    if request.method == 'POST':
        job_title = request.POST['job_title']
        location = request.POST['location']
        job_region = request.POST['job_region']
        job_type = request.POST['job_type']
        job_description = request.POST['job_description']
        company_name = request.POST['company_name']
        tagline = request.POST['tagline']
        company_description = request.POST['job_description1']
        website = request.POST['website']
        email = request.POST['email']
        facebook_username = request.POST['facebook_username']
        twitter_username = request.POST['twitter_username']
        linkedin_username = request.POST['linkedin_username']
        # Extract file data from request.FILES
        featured_image = request.FILES.get('featured_image')
        company_logo = request.FILES.get('company_logo')
        record =JobPosting.objects.create(
        job_title=job_title,
        location=location,
        job_region=job_region,
        job_type=job_type,
        job_description=job_description,
        company_name=company_name,
        tagline=tagline,
        company_description=company_description,
        website=website,
        email=email,
        facebook_username=facebook_username,
        twitter_username=twitter_username,
        linkedin_username=linkedin_username,
        featured_image=featured_image,
        company_logo=company_logo)
        # Sve the new JobPosting instance to the database
        # print()
        record.save()
        print(record)
        return redirect('successs')
    else:
        return render(request,'post-job.html')
    



    
def success(request):
    details = JobPosting.objects.all()
    context = {'jobs':details}

    return render(request,'success.html',context)

def logout_view(request):
    logout(request)
    return redirect('UserHome') 