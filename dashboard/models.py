from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Customers(AbstractUser):
    ordered = models.IntegerField(blank=True, default=0)
    phone = models.CharField(max_length=10, blank=True)
    groups = models.ManyToManyField(User, related_name='customer', blank=True)
    user_permissions = models.ManyToManyField(User, related_name='my_customer_permissions', blank=True)
    	
    last_order = models.CharField(max_length=100, blank=True)

class Mail(models.Model):
    STATE = (
        ('inbox', 'inbox'),
        ('draft', 'draft'),
        ('favourite', 'favourite'),
        ('sent', 'sent'),
        ('spam', 'spam'),
        ('trash', 'trash'),
        ('all_mails', 'all mails')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mail')
    subject = models.CharField(max_length=120)
    to = models.EmailField(help_text='Recipient')
    from_email = models.EmailField()
    messege = models.TextField()
    state = models.CharField(max_length=120, choices=STATE)

    def __str__(self):
        return ('Mail for {}').format(self.user.username)

class Setting(models.Model):
    store_name = models.CharField(max_length=120, blank=True, default='')
    site_email = models.EmailField(blank=True, default='')
    site_copyright = models.CharField(max_length=250, blank=True, default='')
    allow_registration = models.BooleanField(blank=True, default=True)
    main_website = models.URLField(blank=True, default='')
    maintanance_mode = models.BooleanField(blank=True, default=False)

    # Pay fast settings

    merchant_id = models.CharField(max_length=120, blank=True, default='')
    merchant_key = models.CharField(max_length=120, blank=True, default='')

    def __str__(self):
        return self.stmore_name


class Sale(models.Model):
    total_sales = models.IntegerField(blank=True, default=0)
    averarge_order = models.IntegerField(blank=True, default=0)
    orders = models.IntegerField(blank=True, default=0)
    customers = models.IntegerField(blank=True, default=0)
    slug = models.SlugField(blank=True, default='sales')

    def __str__(self):
        return ('my dashboard')