##from django.db import models
##from django.core.validators import DecimalValidator
 
##class Owner(models.Model):
##    owner_id = models.CharField(primary_key=True, max_length=30)
##    first_name = models.CharField(max_length=50, null=False)
##    last_name = models.CharField(max_length=50, null=False)
##    invoice = models.ManyToManyField("InvoiceSale", blank=True)
 
##    class Meta:
##        verbose_name_plural = "Owners"
##        db_table = "Owner"
 
##    def __str__(self):
##            return f"{self.first_name} {self.last_name}"
 
##class InvoiceSale(models.Model):
##    invoice_id = models.CharField(primary_key=True, max_length=30)
##    date = models.DateField()
##    Invoice_type = models.ForeignKey('InvoiceType', verbose_name='InvoiceTypes', on_delete=models.PROTECT)
 
##    class Meta:
##        verbose_name_plural = "IInvoiceSales"
##        db_table = "InvoiceSales"
##        ordering = ("invoice_id",)
    
##    def __str__(self):
##            return f"Invoice - {self.invoice_id} - {self.date}"
 
##class InvoiceType(models.Model):
##    make = models.CharField(max_length=60)
##    model = models.CharField(max_length=150)
##    year = models.IntegerField()
##    color = models.CharField(default='Unknown', max_length=50)
##    price = models.DecimalField(null=False , decimal_places=2, max_digits=10, validators=[DecimalValidator(10, 2)])
##    description = models.TextField(null=True)
 
##    class Meta:
##        verbose_name_plural = "InvoiceTypes"
##        db_table = "InvoiceType"
 
##    def __str__(self):
##           return f"{self.make} {self.model}"