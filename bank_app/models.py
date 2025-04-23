from django.db import models

# Create your models here.

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    online_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def balance(self):
        return self.cash_balance + self.online_balance

    def __str__(self):
        return f"{self.name} — {self.balance}$ (Cash: {self.cash_balance}$, Online: {self.online_balance}$)"