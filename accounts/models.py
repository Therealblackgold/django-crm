from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.utils.text import slugify
from website.models import Package

STATUS_CHOICES = (
    ('pending', 'pending'),
    ('active', 'active'),
    ('deceased', 'deceased'),
    ('cancelled', 'cancelled'),
)


# Member
class Member(AbstractUser):
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default="pending")
    package = models.ForeignKey(Package,
                                max_length=15,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    id_number = models.CharField(max_length=13, unique=True)
    phone_number = models.CharField(max_length=11)
    phone_number_2 = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=500)
    id_copy = models.FileField(upload_to='files/identity_docs/', blank=True)
    proof_of_address = models.FileField(upload_to='files/address_docs/',
                                        blank=True)
    recieved_by = models.CharField(max_length=250, default='online')
    created = models.DateTimeField(auto_now_add=True)
    burial_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.first_name


def member_slug(instance, new_slug=None):
    slug = slugify(instance.id_number)
    if new_slug is not None:
        slug = new_slug
    qs = Member.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%$-%$" % (slug, qs.first().id)
        return member_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Member_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = member_slug(instance)


pre_save.connect(pre_save_Member_receiver, sender=Member)

PERSONAL_INFO_CHOICES = (
    ('active', 'active'),
    ('deceased', 'deceased'),
)


# Personal Info/Base Model
class PersonalInfo(models.Model):
    status = models.CharField(max_length=15,
                              choices=PERSONAL_INFO_CHOICES,
                              default="active")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    phone_number_2 = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    burial_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.first_name


# Members Spouse
class Spouse(PersonalInfo):
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE,
                               related_name='spouse')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.first_name


def spouse_slug(instance, new_slug=None):
    slug = slugify(instance.id_number)
    if new_slug is not None:
        slug = new_slug
    qs = Spouse.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%$-%$" % (slug, qs.first().id)
        return spouse_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Spouse_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = spouse_slug(instance)


pre_save.connect(pre_save_Spouse_receiver, sender=Spouse)


# Members Family
class Family(PersonalInfo):
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE,
                               related_name='family')
    slug = models.SlugField(unique=True)


def fam_slug(instance, new_slug=None):
    slug = slugify(instance.id_number)
    if new_slug is not None:
        slug = new_slug
    qs = Family.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%$-%$" % (slug, qs.first().id)
        return fam_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Family_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = fam_slug(instance)


pre_save.connect(pre_save_Family_receiver, sender=Family)
