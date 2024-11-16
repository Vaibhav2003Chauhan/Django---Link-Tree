from django.shortcuts import render,HttpResponse
import logging
#admin id pass is vishu

#Angela Angela@1234
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import *

from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from home.forms import *
# Create your views here.
def index(request):
    return render(request,'login.html')

def home(request):
    userinfo=request.user.userinformation
    context={'userinfo':userinfo}
    return render(request,'profile.html',context)

# Configure logging (you can customize this as needed)
logger = logging.getLogger(__name__)

def loginUser(request):
    try:
        if request.method == "POST":
            # Check credentials
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            print(username, password, email)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                try:
                    userinfo = userinformation.objects.get(user=user)
                    print(userinfo)
                    context = {'userinfo': userinfo}
                    return render(request, 'profile.html', context)
                except userinformation.DoesNotExist:
                    messages.error(request, "User information not found.")
                    return render(request, 'login.html')

            else:
                messages.info(request, "E-Mail ID or Password was incorrect!")
                return render(request, 'login.html')

    except Exception as e:
        # Log the error for debugging
        logger.error(f"An error occurred during login: {e}", exc_info=True)
        
        # Show a user-friendly error message
        messages.error(request, "An unexpected error occurred. Please try again later.")
        return render(request, 'login.html')

# signup view 
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(username,password,email)
      
        if len(password)<8 :
            messages.warning(request,"password must be of minimum 8 characters ")
        else :
            if password==cpassword:
                if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                    messages.warning(request,"User name or Email was not unique please choose another one")
               
                    return render(request,'signup.html')
                else :
                    user=User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    userinformation.objects.create(
                                        user=user,
                                        mail=email,
                                        name=username,
                                        role="Engineer",
                                        description="------",
                                        phone="------",
                                        github="------",
                                        hackerrank="------",
                                        portfolio="------",
                                        LeetCode="------",
                                        GFG="------",
                                        insta="------",
                                        Linkedin="------",
                                        twitter="------",
                                        facebook="------",
                                        Resume="------",
                                        codepen="------",
                                        website="------",
                                        codechef="------",
                                    )

                    
                    
                    messages.success(request, "Profile created sucessfully.")
                    return render(request,'login.html')
            else :
                messages.warning(request,'Both passwords do not match Kindly check them')
                return  render(request,'signup.html')

        
    return render(request,'signup.html')

def developerprofile(request):
    return render(request,"developer.html")

def logoutuser(request):
    logout(request)

    return render(request,'login.html')


def update(request):
    if request.method=='POST':
        name=request.POST.get('username')
        description=request.POST.get('description')
        # phone=request.POST.get('phone')
        # github=request.POST.get('github')
        # hackerrank=request.POST.get('hackerrank')
        # portfolio=request.POST.get('portfolio')
        # LeetCode=request.POST.get('leetcode')
        # Gfg=request.POST.get('gfg')
        # insta=request.POST.get('insta')
        # Linkedin=request.POST.get('linkedin')
        # twitter=request.POST.get('twitter')
        # facebook=request.POST.get('facebook')
        # Resume=request.POST.get('resume')
        # codepen=request.POST.get('codepen')
        # profile_pic=request.FILES.get('image')
        # website=request.POST.get('website')
        # codechef=request.POST.get('codechef')
        # role=request.POST.get('role')
        print(name)
        print("CREATE")
        # This point handles or put user instance in the newdet varible so that no integrity constraint failed 
        id=request.user.userinformation.id 
        print(description)
        print("is description")
        newdet=userinformation.objects.get(id=id)
        
        print(newdet)
        # saving data in that instance easily 
        newdet.name=request.POST.get('username')
        newdet.description=request.POST.get('description')
        newdet.phone=request.POST.get('phone')
        newdet.profile_pic=request.FILES.get('image')
        newdet.github=request.POST.get('github')
        newdet.hackerrank=request.POST.get('hackerrank')
        newdet.portfolio=request.POST.get('portfolio')
        newdet.LeetCode=request.POST.get('leetcode')
        newdet.GFG=request.POST.get('gfg')
        newdet.insta=request.POST.get('insta')
        newdet.Linkedin=request.POST.get('linkedin')
        newdet.twitter=request.POST.get('twitter')
        newdet.facebook=request.POST.get('facebook')
        newdet.Resume=request.POST.get('resume')
        newdet.codepen=request.POST.get('codepen')
        newdet.website=request.POST.get('website')
        newdet.codechef=request.POST.get('codechef')
        newdet.role=request.POST.get('role')   
        newdet.save()
        userinfo=request.user.userinformation
        context={'userinfo':userinfo}
        return render(request,'profile.html',context)
    return render(request,'index.html')


# def create(request):
#     if request.method=='POST':
#         name=request.POST.get('username')
#         description=request.POST.get('description')
#         phone=request.POST.get('phone')
#         github=request.POST.get('github')
#         hackerrank=request.POST.get('hackerrank')
#         portfolio=request.POST.get('portfolio')
#         LeetCode=request.POST.get('leetcode')
#         Gfg=request.POST.get('gfg')
#         insta=request.POST.get('insta')
#         Linkedin=request.POST.get('linkedin')
#         twitter=request.POST.get('twitter')
#         facebook=request.POST.get('facebook')
#         Resume=request.POST.get('resume')
#         codepen=request.POST.get('codepen')
#         profile_pic=request.FILES.get('image')
#         website=request.POST.get('website')
#         codechef=request.POST.get('codechef')
#         role=request.POST.get('role')
#         print(name)
#         print("CREATE")
#         print(description)
#         print("is description")
#         # This point handles or put user instance in the newdet varible so that no integrity constraint failed 
#         id=request.user.userinformation.id 
#         print("userid")
#         print(id)
#         newdet=userinformation.objects.get(id=id)
        
#         print(newdet)
#         # saving data in that instance easily 
#         newdet.name=name
#         newdet.description=description
#         newdet.phone=phone
#         newdet.profile_pic=profile_pic
#         newdet.github=github
#         newdet.hackerrank=hackerrank
#         newdet.portfolio=portfolio
#         newdet.LeetCode=LeetCode
#         newdet.GFG=Gfg
#         newdet.insta=insta
#         newdet.Linkedin=Linkedin
#         newdet.twitter=twitter
#         newdet.facebook=facebook
#         newdet.Resume=Resume
#         newdet.codepen=codepen
#         newdet.website=website
#         newdet.codechef=codechef
#         newdet.role=role
      
       
        
#         newdet.save()
       
#         userinfo=request.user.userinformation
#         context={'userinfo':userinfo}
#         return render(request,'profile.html',context)
#     return render(request,'create.html')


        
     

   