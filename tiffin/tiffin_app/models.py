# tiffin_app/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class TiffinServiceProvider(models.Model):
    MEAL_TYPE_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NON_VEG', 'Non-Vegetarian'),
        ('BOTH', 'Both Veg & Non-Veg'),
    ]

    name = models.CharField(_("Service Provider Name"), max_length=200)
    owner_name = models.CharField(_("Owner Name"), max_length=150)
    contact_number = models.CharField(_("Contact Number"), max_length=15)
    email = models.EmailField(_("Email"), unique=True)
    operating_city_area = models.CharField(_("Operating City/Area"), max_length=255,
                                         help_text="e.g., Mumbai - Andheri, Pune - Kothrud")
    meal_type_offered = models.CharField(
        _("Type of Meal Offered"),
        max_length=10,
        choices=MEAL_TYPE_CHOICES,
        default='VEG'
    )
    delivery_options = models.TextField(
        _("Delivery Options"),
        help_text="e.g., Free delivery within 5km, Chargeable beyond, Specific timings"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tiffin Service Provider")
        verbose_name_plural = _("Tiffin Service Providers")
        ordering = ['name']

class MealPackage(models.Model):
    MEAL_TYPE_CHOICES = [
        ('LUNCH', 'Lunch'),
        ('DINNER', 'Dinner'),
        ('BOTH', 'Both Lunch & Dinner'),
    ]
    DURATION_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
    ]

    tiffin_service_provider = models.ForeignKey(
        TiffinServiceProvider,
        on_delete=models.CASCADE,
        related_name='meal_packages',
        verbose_name=_("Associated Tiffin Service")
    )
    package_name = models.CharField(_("Package Name"), max_length=200)
    description = models.TextField(_("Description"))
    meal_type = models.CharField(
        _("Meal Type (Lunch/Dinner)"),
        max_length=10,
        choices=MEAL_TYPE_CHOICES,
        default='LUNCH'
    )
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    duration = models.CharField(
        _("Duration"),
        max_length=10,
        choices=DURATION_CHOICES,
        default='WEEKLY'
    )
    service_area_city = models.CharField(
        _("Area/City of Service for this Package"),
        max_length=255,
        help_text="e.g., Mumbai - Andheri West. Be specific for filtering."
    )
    image = models.ImageField(
        _("Package Image"),
        upload_to='meal_package_images/',
        blank=True,
        null=True,
        help_text="Optional: A representative image of the meal package."
    )
    is_active = models.BooleanField(_("Is Active?"), default=True,
                                  help_text="Uncheck to hide this package from public view.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.package_name} by {self.tiffin_service_provider.name}"

    class Meta:
        verbose_name = _("Meal Package")
        verbose_name_plural = _("Meal Packages")
        ordering = ['-created_at', 'package_name']