from django.contrib import admin
from .models import AppVariety, AppReview, AppStore, AppCertificate
class AppReviewInLine(admin.TabularInline):
    model = AppReview
    extra = 2

class AppVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [AppReviewInLine]

class AppStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varieties', )

class AppCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'certificates_number')

admin.site.register(AppVariety, AppVarietyAdmin)
admin.site.register(AppStore, AppStoreAdmin)
admin.site.register(AppCertificate, AppCertificateAdmin)
