from django.contrib import admin
from .models import Entertainment, Sport, Business, Technology, Health, Celebrities, LifeStyle, BreakingNews

admin.site.site_header = "Add New Post"


class PostAdmin(admin.ModelAdmin):
    list_display = ("publisher", "title",  "time", "date")
    search_fields = ['title', 'description']


admin.site.register(Entertainment, PostAdmin)
admin.site.register(Sport, PostAdmin)
admin.site.register(Business, PostAdmin)
admin.site.register(Technology, PostAdmin)
admin.site.register(Health, PostAdmin)
admin.site.register(Celebrities, PostAdmin)
admin.site.register(LifeStyle, PostAdmin)
admin.site.register(BreakingNews, PostAdmin)
