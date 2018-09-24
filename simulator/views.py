# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
import os
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth import authenticate, login, logout
from .models import  Student, Teacher


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('first_view')
        return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('login')

class UserRegister(View):
    form_class = UserForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email'] 
            user.is_active = True
            user.set_password(password)
            print(password+"vjh")
            user.save()
            message = "registered successfully"
            login(request, user)
            return redirect('choose')
        return render(request, self.template_name, {'form':form})

def StudentRegister(request):
	student = Student()
	student.user = request.user
	student.save()
	return redirect('login')

def TeacherRegister(request):
	teacher = Teacher()
	teacher.user = request.user
	teacher.save()
	return redirect('login')

def first_view(request):
    return render(request,'test.html',{})

def choose_view(request):
    return render(request, 'choose.html',{})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(('/profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'profile_edit.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })