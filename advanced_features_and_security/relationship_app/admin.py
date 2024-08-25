from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
#from .models import CustomUser

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "role"]

admin.site.register(UserProfile, UserProfileAdmin)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     # fieldsets is used to define how fields are grouped when you view or edit a user in the admin panel.
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {"fields": ("date_of_birth", "profile_photo")}),
#     )

#     # add_fieldsets is used to define how fields are grouped on the user creation form in the admin panel.
#     add_fieldsets = UserAdmin.fieldsets + (
#         (None, {"fields": ("date_of_birth", "profile_photo")}),
#     )
#     list_display = ["username",
#                     "email",
#                     "first_name",
#                     "last_name",
#                     "date_of_birth",
#                     "profile_photo"]

# admin.site.register(CustomUser, CustomUserAdmin)