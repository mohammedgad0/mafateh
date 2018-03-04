from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


# Create your models here.

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Product(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=125)  # Field name made lowercase.
    descreption = models.CharField(db_column='Descreption', max_length=500,null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=10)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=128,unique='True')  # Field name made lowercase.
    image = models.ImageField(upload_to = 'products_folder/',db_column='Image',null=True)
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    available = models.IntegerField(db_column='Available',null=True,blank=True,)  # Field name made lowercase.
    mainprice = models.DecimalField(db_column='MainPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    def __str__(self):
        return u'{0}'.format(self.itemcode)
    class Meta:
        managed = False
        db_table = 'product'

class Customer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=25)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return u'{0}'.format(self.name)
    class Meta:
        managed = False
        db_table = 'customer'

class Invoice_details(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    invoicenumber = models.ForeignKey('Invoice',to_field='invoice_number',db_column='InvoiceNumber',on_delete=models.DO_NOTHING,blank=True,null=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', to_field='itemcode',db_column='ProductId',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    itemprice = models.DecimalField(db_column='ItemPrice', max_digits=8, decimal_places=2)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=10)  # Field name made lowercase.
    total_before_discount = models.DecimalField(db_column='total_before_discount', max_digits=8, decimal_places=2)  # Field name made lowercase.
    total_after_discount = models.DecimalField(db_column='total_after_discount', max_digits=8, decimal_places=2)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'invoice_details'
def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 'INV-00001'
    invoice_no = last_invoice.invoice_number
    invoice_int = int(invoice_no.split('INV-')[-1])
    width = 5
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'INV-' + str(formatted)
    return new_invoice_no


class Invoice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # invoicenumber = models.CharField('Invoice',db_column='InvoiceNumber',unique=True, max_length=64)  # Field name made lowercase.
    # invoice_number = models.CharField(db_column='InvoiceNumber',unique=True, max_length=64,blank=True, null=True)  # Field name made lowercase.
    invoice_number = models.CharField(db_column='InvoiceNumber',max_length=100, blank=True, unique=True, default=increment_invoice_number)

    customerid = models.ForeignKey('Customer',db_column='CustomerId',on_delete=models.DO_NOTHING,blank=True, null=True)  # Field name made lowercase.
    total_before_discount = models.DecimalField(db_column='total_before_discount', max_digits=8, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    total_after_discount = models.DecimalField(db_column='total_after_discount', max_digits=8, decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    final_price = models.DecimalField(db_column='Final_Price', max_digits=8, decimal_places=2,blank=True, null=True)
    # totalprice = models.CharField(db_column='TotalPrice', max_length=10,blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='invoice_date',blank=True, null=True)
    emp_id = models.ForeignKey('AuthUser',db_column='emp_id',on_delete=models.DO_NOTHING,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'

class Media(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Product',db_column='ItemId',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    image = models.ImageField(upload_to = 'pic_folder/',db_column='Image',null=True)



    class Meta:
        managed = False
        db_table = 'media'
