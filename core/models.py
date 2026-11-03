
from django.db import models
from django.core.validators import FileExtensionValidator


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ('Programming', 'Language'),
        ('Database', 'Database'),
        ('AI/ML', 'AI/ML'),
        ('Tools', 'Tools'),
        ('Frameworks', 'Frameworks'),
        ('DEVOPS & CLOUD', 'DEVOPS & CLOUD'),

    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )


    description = models.CharField(
        max_length=200,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(max_length=150)

    description = models.TextField()

    technologies = models.JSONField(
        default=list,
        blank=True,
        help_text='Example: ["Python", "Django", "MySQL"]'
    )

    github_url = models.URLField(blank=True)

    live_url = models.URLField(blank=True)

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)

    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)

    cgpa = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    is_current = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"




class Resume(models.Model):

    title = models.CharField(
        max_length=100,
        default="My Resume"
    )

    file = models.FileField(
        upload_to="resumes/",
        validators=[FileExtensionValidator(['pdf'])]
    )

    uploaded_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title




class About(models.Model):

    name = models.CharField(max_length=100)

    short_intro = models.CharField(max_length=250)

    description = models.TextField()

    career_objective = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    email = models.EmailField(blank=True)

    is_active = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.name


class WebsiteSettings(models.Model):

    site_name = models.CharField(
        max_length=100,
        default="Rohit Kumar Rawat"
    )

    logo_text = models.CharField(
        max_length=50,
        default="RKR"
    )

    tagline = models.CharField(
        max_length=200,
        blank=True
    )

    footer_text = models.CharField(
        max_length=250,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    copyright_year = models.PositiveIntegerField(
        default=2026
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Website Settings"
        verbose_name_plural = "Website Settings"

    def __str__(self):
        return self.site_name
    site_name = models.CharField(
        max_length=100,
        default="Rohit Kumar Rawat"
    )

    logo_text = models.CharField(
        max_length=50,
        default="RKR"
    )

    tagline = models.CharField(
        max_length=200,
        blank=True
    )

    footer_text = models.CharField(
        max_length=250,
        blank=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website Settings"
        verbose_name_plural = "Website Settings"

    def __str__(self):
        return self.site_name

class NavigationLink(models.Model):
    title = models.CharField(max_length=50)

    url = models.CharField(
        max_length=200,
        help_text="Example: #about or /contact/"
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title