from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title','footer_link_box', 'url']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']

class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.FooterLink, FooterLinkAdmin)
admin.site.register(models.SiteBanner, SiteBannerAdmin)