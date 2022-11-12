from django.db import models

class CustomManager(models.Manager):
    def all_records_in_desc_price_order(request):
        return super().order_by('-price')
