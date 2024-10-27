from django.contrib import admin
from core.models import ConfigItem
from core.models import GlobalConfig

admin.site.register(ConfigItem)
admin.site.register(GlobalConfig)