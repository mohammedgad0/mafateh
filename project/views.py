from django.shortcuts import render, render_to_response ,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse ,HttpResponseRedirect,Http404 ,HttpResponseForbidden
from django.urls import reverse
from .forms import *
from .models import *
from django.conf import settings
from django.utils import translation
from django.forms import formset_factory
from django.http import JsonResponse
from django.core import serializers
import json
from datetime import datetime , timedelta
from django.contrib.auth.models import User,Group
from django.forms import modelformset_factory
from django.core.cache import cache

# Create your views here.


def Index(request):
    product = Product.objects.all()
    context = {'LANG': request.LANGUAGE_CODE,'product':product}
    return render(request, 'project/home.html',context)


def Productpopup(request, id):
    product = get_object_or_404(Product , id = id)
    context = {'LANG': request.LANGUAGE_CODE,'product':product}
    return render(request, 'project/product_popup.html',context)

def add_invoice(request):
    request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    translation.activate(request.LANG)
    request.LANGUAGE_CODE = request.LANG
    query = Invoice_details.objects.none()
    form = addinvoice
    invoice_details = modelformset_factory(Invoice_details, form=invoicedetails, extra=20)
    # formset = formset(queryset=Invoice_details.objects.filter(id= 15))
    # formset = formset_factory(invoicedetails, extra=20)
    formset = invoice_details(request.POST or None,queryset=query)
    if request.method == 'POST':
        print("is post request")
        form = addinvoice(request.POST or None)
        if form.is_valid() and formset.is_valid():
            print("form is valid")
            inv_obj = formset.save(commit=False)
            invoice_obj = form.save(commit=False)

            invoice_obj.customerid = Customer.objects.filter(id= invoice_obj.customerid.id).get()
            invoice_obj.empid =  User.objects.get(id=request.user.id)
            invoice_obj.invoicedate = datetime.now()
            vat = int(invoice_obj.total_after_discount) * 5 / 100
            print(int(invoice_obj.total_after_discount) - vat)
            invoice_obj.final_price = int(invoice_obj.total_after_discount) + vat
            invoice_obj.save()

            for obj in inv_obj:
                # obj.invoicenumber = invoice_obj.invoice_number
                obj.invoicenumber = Invoice.objects.filter(invoice_number= invoice_obj.invoice_number).get()
                # price_before_discount.append(obj.total_before_discount)
                # price_after_discount.append(obj.total_after_discount)
                obj.save()
            return HttpResponseRedirect(reverse('project:view-invoice' , kwargs={'inv_no':invoice_obj.invoice_number} ))

    else:
        form = form
        formset = formset
    context ={'form':form, 'formset':formset}
    return render(request, 'project/invoice_add.html',context)

def load_product(request):
    item_id = request.GET.get('country')
    product = get_object_or_404(Product, itemcode=item_id)
    data = serializers.serialize('json', [product])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type='application/json')

def loadCustomer(request):
    customer_number = request.GET.get('customer')
    customer = get_object_or_404(Customer, mobile=customer_number)
    data = serializers.serialize('json', [customer])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type='application/json')

def viewInvoice(request , inv_no):
    request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    translation.activate(request.LANG)
    invoice = get_object_or_404(Invoice , invoice_number = inv_no)
    inv_details = Invoice_details.objects.filter(invoicenumber = inv_no)
    cache.set('invoice', 'invoice', 30)
    cache.set('inv_details', 'inv_details', 30)
    context ={'invoice':invoice,'inv_details':inv_details}
    return render(request, 'project/invoice_view.html',context)

def allInvoice(request):
    request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    translation.activate(request.LANG)
    all_invoice = Invoice.objects.all()
    context= {"all_invoice":all_invoice}
    return render(request, 'project/invoice_all.html',context)


def updateInvoice(request, inv_no):
    request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    translation.activate(request.LANG)
    instance = get_object_or_404(Invoice, invoice_number=inv_no)
    form = addinvoice(initial={'customer_number':instance.customerid.mobile,'customer_name':instance.customerid.name
    ,'invoice_date':instance.invoicedate,'emp_name':instance.emp_id.first_name
    })
    query = Invoice_details.objects.filter(invoicenumber = inv_no)
    invoice_details = modelformset_factory(Invoice_details, form=invoicedetails, extra=20)
    formset = invoice_details(request.POST or None,queryset=query)
    if request.method == 'POST':
        print("is post request")
        form = addinvoice(request.POST or None ,instance=instance)
        if form.is_valid() and formset.is_valid():
            print("form is valid")
            inv_obj = formset.save(commit=False)
            invoice_obj = form.save(commit=False)

            invoice_obj.customerid = Customer.objects.filter(id= invoice_obj.customerid.id).get()
            invoice_obj.empid =  User.objects.get(id=request.user.id)
            invoice_obj.invoicedate = datetime.now()
            vat = int(invoice_obj.total_after_discount) * 5 / 100
            print(int(invoice_obj.total_after_discount) - vat)
            invoice_obj.final_price = int(invoice_obj.total_after_discount) + vat
            invoice_obj.save()

            for obj in inv_obj:
                # obj.invoicenumber = invoice_obj.invoice_number
                obj.invoicenumber = Invoice.objects.filter(invoice_number= invoice_obj.invoice_number).get()
                # price_before_discount.append(obj.total_before_discount)
                # price_after_discount.append(obj.total_after_discount)
                obj.save()
            return HttpResponseRedirect(reverse('project:view-invoice' , kwargs={'inv_no':invoice_obj.invoice_number} ))
    else:
        formset = formset
    context ={'form':form, 'formset':formset}
    return render(request, 'project/invoice_update.html',context)
def html_to_pdf_view(request):
    request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    translation.activate(request.LANG)
    from django.core.files.storage import FileSystemStorage
    from django.http import HttpResponse
    from django.template.loader import render_to_string

    from weasyprint import HTML
    invoice = cache.get('invoice')
    inv_details = cache.get('inv_details')
    invoice = get_object_or_404(Invoice , invoice_number = "INV-00005")
    inv_details = Invoice_details.objects.filter(invoicenumber = "INV-00005")
    context ={'invoice':invoice,'inv_details':inv_details}
    paragraphs = {'invoice':invoice,'inv_details':inv_details}
    html_string = render_to_string('project/invoice_print.html', context)

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response
