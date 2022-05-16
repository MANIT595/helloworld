from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import *

admin.site.register(Users),
admin.site.register(Post),
admin.site.register(Friends),
admin.site.register(Notification),
admin.site.register(Messages),
admin.site.register(Payment)
