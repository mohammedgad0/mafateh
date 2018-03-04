from django import forms
from .models import *
from django.forms import ModelForm, Textarea,TextInput,DateField
from django.utils.translation import ugettext_lazy as _

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class addinvoice(ModelForm):
      customer_number = forms.CharField(label=_('Customer number'),widget=forms.TextInput(attrs={'class': 'form-control js-text'} ))
      customer_name = forms.CharField(label=_('Customer Name'),widget=forms.TextInput(attrs={'class': 'form-control '} ))
      emp_name = forms.CharField(label=_('Employee Name'),widget=forms.TextInput(attrs={'class': 'form-control '} ))
      invoice_date = forms.CharField(label=_('Invoice Date'),widget=forms.TextInput(attrs={'class': 'form-control '} ))
      class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'customerid':forms.TextInput(attrs={'class': 'form-control hidden','placeholder':_('Customer Name')}),
            # 'customerid':TextInput(attrs={'class': 'form-control','placeholder':_('Customer Name'),'required': True}),
            'invoicedate':TextInput(attrs={'class': 'form-control hidden','placeholder':_('Invoice Date'),'required': True}),
            'total_before_discount':TextInput(attrs={'class': 'form-control hidden','required': False}),
            'total_after_discount':TextInput(attrs={'class': 'form-control hidden','required': False}),
            # 'emp_id':forms.Select(attrs={'class': 'form-control','placeholder':_('Customer Name')}),
            'emp_id':TextInput(attrs={'class': 'form-control hidden','placeholder':_('Employee Name'),'required': True}),

        }
        labels = {
            'customerid': _('Customer Name'),
            'invoicedate': _('Invoice Date'),
            'emp_id':_('Employee Name'),

        }

class invoicedetails(ModelForm):
      name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','label':_("Name"),'placeholder':_("Name")}),required=False, max_length=250)
      mainprice = forms.CharField(widget=forms.TextInput(attrs={'class': '','label':_("Name"),}),required=False, max_length=20)

      class Meta:
        model = Invoice_details
        fields = '__all__'
        widgets = {
            'productid':forms.Select(attrs={'class': 'js-select form-control','placeholder':_('Product Id')}),
            # 'customerid':TextInput(attrs={'class': 'form-control','placeholder':_('Customer Name'),'required': True}),
            'name':TextInput(attrs={'class': 'form-control','placeholder':_('quantity'),'required': True}),
            'mainprice':TextInput(attrs={'class': 'form-control','placeholder':_('quantity'),'required': True}),
            'quantity':TextInput(attrs={'class': 'form-control','placeholder':_('quantity'),'required': True}),
            # 'emp_id':forms.Select(attrs={'class': 'form-control','placeholder':_('Customer Name')}),
            'itemprice':TextInput(attrs={'class': 'form-control','placeholder':_('item price'),'required': True}),
            'discount':TextInput(attrs={'class': 'form-control','placeholder':_('discount'),'required': False}),
            'total_before_discount':TextInput(attrs={'class': 'form-control','placeholder':_('total after price'),'required': True}),
            'total_after_discount':TextInput(attrs={'class': 'form-control','placeholder':_('total before price'),'required': True}),


        }
        labels = {
            'productid': _('Product Id'),
            'quantity': _('quantity'),
            'name': _('Name'),
            'itemprice':_('item price'),
            'discount':_('discount'),
            'totalprice':_('totalprice'),

        }
