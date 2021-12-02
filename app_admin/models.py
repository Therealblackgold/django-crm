from django.db import models
from djmoney.models.fields import MoneyField
from accounts.models import Member

MONTH_CHOICES = (
    ('Undefined', 'Undefined'),
    ('Jan', 'Jan'),
    ('Feb', 'Feb'),
    ('Mar', 'Mar'),
    ('Apr', 'Apr'),
    ('May', 'May'),
    ('Jun', 'Jun'),
    ('Jul', 'Jul'),
    ('Aug', 'Aug'),
    ('Sep', 'Sep'),
    ('Oct', 'Oct'),
    ('Nov', 'Nov'),
    ('Dec', 'Dec'),
)


# Member payments
class Payment(models.Model):
    member = models.ForeignKey(Member,
                               related_name='paid',
                               on_delete=models.CASCADE)
    amount = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='ZAR',
        max_digits=11,
    )
    month = models.CharField(max_length=15,
                             choices=MONTH_CHOICES,
                             default="Undefined")
    proof_of_payment = models.FileField(upload_to='payments/%Y/%m/%d',
                                        blank=True,
                                        null=True)

    date = models.DateTimeField(auto_now_add=True)
