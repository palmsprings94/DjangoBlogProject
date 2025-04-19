from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import additionalforms

def register(request):
    form = additionalforms()
    if request.method == 'POST':
        form = additionalforms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account made - {username}")
            return redirect('login')

    context = {'formz': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    username = f"{request.user.username[:1].upper()}{request.user.username[1:]}"
    context = {'title': username, 'username': username}
    return render(request, 'users/profile.html', context)
