from django.contrib import admin
from note.models import Note
# our class containing more infos about User
from note.models import UserProfile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# with this class
# We will display the user profile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# redefine the UserAdmin class
# used by the admin interface
# and link the stacked inlines
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

# Register your models here.
admin.site.register(Note)
# re register the UserAdmin to take care of the stacked inlines
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
