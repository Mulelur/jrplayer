from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Shipping, TrackOrder
from django.urls import reverse
from cart.models import Order
from django.forms import inlineformset_factory
from .forms import UserRegisterForm, UserShippingForm, EditProfileForm, PasswordProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import views
from home.models import Banner


    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account Has Benn Created! {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    template = 'account/register.html'

    context = {
        'form': form
    }
    return render(request, template, context)

@login_required
def profile(request):
    template = 'account/profile.html'

    return render(request, template)

@login_required
def my_account(request):
    banner = Banner.objects.get(title='my-account')
    template = 'account/my_account.html'

    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)

    context = {
        'my_orders': my_orders,
        'banner': banner
    }

    return render(request, template, context)


# def delivery(request):
#     template = 'account/delivery.html'
#     form = UserShippingForm()
#     if request.method == 'POST':
#         form = UserShippingForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('delivery'))

#     context = {'form': form}
#     return render(request, template, context)


def edit_profile(request):
    banner = Banner.objects.get(title='edit-profile')
    
    template = 'account/edit_profile.html'
    if request.method == 'POST':
        editform = EditProfileForm(request.POST, instance=request.user)
        passwordform = PasswordProfileForm(
            data=request.POST, user=request.user)

        if editform.is_valid() or passwordform.is_valid():
            editform.save()
            return redirect(reverse('edit_profile'))
        if passwordform.is_valid():
            passwordform.save()
            update_session_auth_hash(request, passwordform.user)
            return redirect(reverse('edit_profile'))
    else:
        passwordform = PasswordProfileForm(user=request.user)
        editform = EditProfileForm(instance=request.user)
        context = {'editform': editform, 'passwordform': passwordform, 'banner': banner}
        return render(request, template, context)
