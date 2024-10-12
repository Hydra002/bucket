from email.policy import default

from django.db import models
from django.db.models import ForeignKey

TXN_TYPES = [
    ("IN", "INCOME"),
    ("EX", "EXPENDITURE"),
    ("TR", "TRANSFER")
]

class TxnCategory(models.Model):
    title = models.CharField(max_length=25)
    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transactions(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    description = models.TextField()
    amount = models.PositiveIntegerField()
    date = models.DateField()
    is_committed = models.BooleanField(default=False)
    txn_type = models.CharField(choices=TXN_TYPES, max_length=5, default="EX")
    category = models.ForeignKey(TxnCategory, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
