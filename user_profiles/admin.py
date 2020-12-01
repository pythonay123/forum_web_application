from django.contrib import admin
from .models import Profile, UserEvaluation


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', Profile.__str__, 'reg_date', 'modified_date', 'summary',)
    search_fields = ['user']

    class Meta:
        model = Profile


class UserEvaluationAdmin(admin.ModelAdmin):
    # readonly_fields = ["number_of_threads_created", "number_of_posts", "profile_views"]
    list_display = ('user', 'user_rating', 'user_level', 'seniority', 'number_of_threads_created', 'number_of_posts',
                    'profile_views',)
    search_fields = ['user']

    class Meta:
        model = UserEvaluation


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserEvaluation, UserEvaluationAdmin)
