from django.contrib import admin
from django.contrib.auth.models import User
from .models import Pet, AdoptionRequest, PetImage, UserProfile


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "species", "status", "created_at")
    list_filter = ("status", "species")
    search_fields = ("name", "description")


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "pet", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("user__username", "pet__name")


@admin.register(PetImage)
class PetImageAdmin(admin.ModelAdmin):
    list_display = ("pet", "image_url", "created_at")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "is_admin",
        "is_superuser",
        "last_login",
        "join_date",
    )
    search_fields = ("user__username", "phone_number")

    def is_admin(self, obj):
        return obj.user.is_staff

    is_admin.boolean = True
    is_admin.short_description = "管理员"

    def is_superuser(self, obj):
        return obj.user.is_superuser

    is_superuser.boolean = True
    is_superuser.short_description = "超级管理员"

    def last_login(self, obj):
        return obj.user.last_login

    last_login.short_description = "最后登录时间"

    def join_date(self, obj):
        return obj.user.date_joined

    join_date.short_description = "注册时间"


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
