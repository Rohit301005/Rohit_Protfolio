
from django.contrib import admin
from .models import About, ContactMessage, Education, NavigationLink, Skill, Project,Resume, WebsiteSettings


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ('name','category','is_active', )

    list_filter = ('category','is_active',)

    search_fields = ('name',)

    list_editable = ('is_active', )




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title','is_featured', 'is_active', 'created_at', )

    list_filter = ( 'is_featured', 'is_active',)

    search_fields = ( 'title', 'description', )

    list_editable = (  'is_featured',  'is_active',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree','institution','start_year', 'end_year', 'is_current', 'is_active',)

    list_filter = ('is_current', 'is_active')
    search_fields = ('degree', 'institution')
    list_editable = ('is_current', 'is_active')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ('name','email', 'subject','is_read','created_at', )

    list_filter = ('is_read', 'created_at')

    search_fields = ('name', 'email', 'subject', 'message', )

    list_editable = ('is_read',)

    readonly_fields = ('created_at',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):

    list_display = ( 'title', 'uploaded_at','is_active',)

    list_filter = ('is_active',)

    search_fields = ('title',)

    list_editable = ('is_active',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'is_active',
        'updated_at'
    )

    list_filter = ('is_active',)

    search_fields = ('name', 'email')

@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        'site_name',
        'logo_text',
        'email',
        'copyright_year',
        'updated_at'
    )

    readonly_fields = ('updated_at',)

    fieldsets = (
        ('Website Branding', {
            'fields': (
                'site_name',
                'logo_text',
                'tagline',
            )
        }),

        ('Contact Information', {
            'fields': (
                'email',
                'github_url',
                'linkedin_url',
            )
        }),

        ('Footer Settings', {
            'fields': (
                'footer_text',
                'copyright_year',
            )
        }),

        ('System Information', {
            'fields': ('updated_at',)
        }),
    )
    list_display = ('site_name', 'logo_text', 'updated_at')
    readonly_fields = ('updated_at',)



@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)