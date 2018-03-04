# Generated by Django 2.0.2 on 2018-02-24 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=128)),
                ('email', models.CharField(db_column='Email', max_length=128)),
                ('mobile', models.CharField(db_column='Mobile', max_length=25)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=128, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('image', models.ImageField(db_column='Image', null=True, upload_to='pic_folder/')),
            ],
            options={
                'db_table': 'media',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=125)),
                ('weight', models.CharField(db_column='Weight', max_length=10)),
                ('itemcode', models.CharField(db_column='ItemCode', max_length=128)),
                ('image', models.ImageField(db_column='Image', null=True, upload_to='products_folder/')),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('available', models.IntegerField(blank=True, db_column='Available', null=True)),
                ('mainprice', models.CharField(db_column='MainPrice', max_length=50)),
                ('saleprice', models.CharField(db_column='SalePrice', max_length=50)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('totalprice', models.CharField(db_column='TotalPrice', max_length=10)),
                ('invoicedate', models.DateTimeField(db_column='invoice_date')),
                ('customerid', models.ForeignKey(db_column='CustomerId', on_delete=django.db.models.deletion.DO_NOTHING, to='project.Customer')),
            ],
            options={
                'db_table': 'invoice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Invoice_details',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('invoicenumber', models.CharField(db_column='InvoiceNumber', max_length=64, unique=True, verbose_name='Invoice')),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('itemprice', models.CharField(db_column='ItemPrice', max_length=10)),
                ('discount', models.CharField(db_column='Discount', max_length=10)),
                ('totalprice', models.CharField(db_column='TotalPrice', max_length=10)),
                ('productid', models.ForeignKey(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, to='project.Product')),
            ],
            options={
                'db_table': 'invoice_details',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoicenumber',
            field=models.ForeignKey(db_column='InvoiceNumber', on_delete=django.db.models.deletion.DO_NOTHING, to='project.Invoice_details', to_field='invoicenumber'),
        ),
    ]