from django.db import models
import barcode                      # additional imports
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):          # overriding save()
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
