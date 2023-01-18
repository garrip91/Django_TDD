from django.shortcuts import render


def register_user(request):
    return render(request, "accounts/register.html", )
