from django.db import models
import re, datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        lowerRegex = re.compile(r'[a-z]+')
        upperRegex = re.compile(r'[A-Z]+')
        digitRegex = re.compile(r'[0-9]+')
        specRegex = re.compile(r'[$&+,:;=?@#|<>.^*()%!-]+')
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name must be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last Name must be at least 2 characters"
        email_list = User.objects.filter(email=postData['email'])
        if len(email_list) > 0:
            errors["email_exists"] = "An account with that email already exists"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
        if len(postData['passwd']) < 8: 
            errors["passwd_char"] = "Password must contain atleast 8 characters"
        if not lowerRegex.findall(postData['passwd']): 
            errors["passwd_low"] = "Password must contain atleast one lowercase character"
        if not upperRegex.findall(postData['passwd']): 
            errors["passwd_up"] = "Password must contain atleast one uppercase character"
        if not digitRegex.findall(postData['passwd']): 
            errors["passwd_num"] = "Password must contain atleast one digit"
        if not specRegex.findall(postData['passwd']): 
            errors["passwd_spec"] = "Password must contain atleast one special character"
        if postData["passwd"] != postData["confirm_passwd"]:
            errors["passwd"] = "Passwords do not match!"
        return errors
    
    def password_validator(self, postData):
        errors = {}
        lowerRegex = re.compile(r'[a-z]+')
        upperRegex = re.compile(r'[A-Z]+')
        digitRegex = re.compile(r'[0-9]+')
        specRegex = re.compile(r'[$&+,:;=?@#|<>.^*()%!-]+')
        if len(postData['passwd']) < 8: 
            errors["passwd_char"] = "Password must contain atleast 8 characters"
        if not lowerRegex.findall(postData['passwd']): 
            errors["passwd_low"] = "Password must contain atleast one lowercase character"
        if not upperRegex.findall(postData['passwd']): 
            errors["passwd_up"] = "Password must contain atleast one uppercase character"
        if not digitRegex.findall(postData['passwd']): 
            errors["passwd_num"] = "Password must contain atleast one digit"
        if not specRegex.findall(postData['passwd']): 
            errors["passwd_spec"] = "Password must contain atleast one special character"
        if postData["passwd"] != postData["confirm_passwd"]:
            errors["passwd"] = "Passwords do not match!"
        return errors
    
    def information_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name must be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last Name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    last_login = models.DateTimeField()

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)