from django.contrib import admin
from django import forms
# Register your models here.
from .models import *

@admin.register(Media)
class MdiaAdmin(admin.ModelAdmin):
    model = Media

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ('name','descreption','weight','itemcode','quantity','available','mainprice','saleprice','image')
    list_display = ('name','weight','itemcode','quantity','available','mainprice','saleprice','image')
    list_per_page=100
    ordering = ['-available']
    search_fields = ['name', 'itemcode']
    show_full_result_count=True
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ProductAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'descreption':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    fields = ('name','email','mobile','address')
    list_display = ('name','email','mobile','address')
    list_per_page=100
    ordering = ['-name']
    search_fields = ['name', 'email']
    show_full_result_count=True

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    fields = ('invoice_number','customerid','invoicedate','emp_id')
    list_display = ('invoice_number','customerid','invoicedate','emp_id')
    list_per_page=100

    show_full_result_count=True
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     model = Employee
#     fk_name = "id"
#     fields = ( 'empname', 'sexcode', 'empid', 'jobtitle', 'deptcode', 'deptname', 'mobile', 'email','ismanager','managercode','ext','iscontract')
#     list_display =( 'empname', 'empid', 'jobtitle', 'deptcode', 'deptname',  'email','ismanager','managercode','ext','iscontract')
#   #  filter_vertical=('deptcode','sexcode')
#     list_filter=('ismanager','iscontract')
#     #list_max_show_all=200
#     list_per_page=100
#     ordering = ['-ismanager','empname']
#     search_fields = ['empname', 'sexcode', 'empid', 'jobtitle', 'deptcode', 'deptname', 'mobile', 'email']
#    # autocomplete_fields=['empname']  #autocomplete_fields is a list of ForeignKey and/or ManyToManyField fields
#     show_full_result_count=True
