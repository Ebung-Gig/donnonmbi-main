from django.contrib import admin

from website.models import News, Team, Trustee


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    search_fields = ("title", "content")
    ordering = ("-published_date",)


class TrusteeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "position",
    )  # Display name, avatar, and position in the admin list view
    search_fields = ("name", "position")  # Allows search by trustee name or position


admin.site.register(Trustee, TrusteeAdmin)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")
