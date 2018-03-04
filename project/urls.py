from django.conf.urls import url ,include
from project import views

#application namespace
app_name = 'project'


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.

    # The home page
    url(r'^$', views.Index, name='index'),
    url(r'^product/(?P<id>\d+)/popup/$', views.Productpopup, name='product-popup'),
    url(r'^add/invoice/$', views.add_invoice, name='add-invoice'),
    url(r'^all/invoice/$', views.allInvoice, name='all-invoice'),
    url(r'^view/invoice/(?P<inv_no>.*)/$', views.viewInvoice, name='view-invoice'),
    url(r'^update/invoice/(?P<inv_no>.*)/$', views.updateInvoice, name='update-invoice'),
    url('ajax/load-cities/', views.load_product, name='ajax_load_product'),
    url('ajax/load-customer/', views.loadCustomer, name='ajax_load_customer'),
    url('invoice/print/', views.html_to_pdf_view, name='html_to_pdf_view'),

]
