from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #сохраняем данные с формы в базу данных
            return redirect('success')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})


def success_view(requset):
    return render(requset, 'success.html')