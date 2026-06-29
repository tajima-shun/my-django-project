from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import timedelta


class User(AbstractUser):
    """Project-local user model. If a project-wide custom user is preferred,
    set AUTH_USER_MODEL in settings to 'apps.bookings.User'."""

    phone_number = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        full_name = self.get_full_name()
        return full_name or self.username


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}{', ' + self.country if self.country else ''}"


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="hotels")
    address = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "city")

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Room(models.Model):
    ROOM_TYPES = (
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default="single")
    capacity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["hotel", "number"]
        unique_together = ("hotel", "number")

    def __str__(self):
        return f"{self.hotel.name} - {self.number} ({self.get_room_type_display()})"


class Booking(models.Model):
    STATUS = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["check_in", "check_out"]) ]

    def clean(self):
        # Enforce the strict 1-night stay rule from AGENTS.md/OpenSpec
        if self.check_in and self.check_out:
            if self.check_out <= self.check_in:
                raise ValidationError("check_out must be after check_in")
            if (self.check_out - self.check_in) != timedelta(days=1):
                raise ValidationError("Bookings must be exactly one night")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking #{self.pk or '?'}: {self.user} - {self.room} on {self.check_in}"
