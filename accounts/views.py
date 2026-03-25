from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.user.is_authenticated:
       return redirect("dashboard")  # Already logged in

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Account created for {username}! You can now log in."
            )
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/dashboard.html")
    
    else:
        return redirect('login')
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html", {})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")
