from django.contrib import admin
from .models import GeneratedPassword
 

@admin.register(GeneratedPassword)
class GeneratedPasswordAdmin(admin.ModelAdmin):
    list_display = ('password', 'length', 'include_numbers', 'include_special_chars', 'generated_at')
    list_filter = ('include_numbers', 'include_special_chars')
    search_fields = ('password',)
    ordering = ('-generated_at',)
                    
