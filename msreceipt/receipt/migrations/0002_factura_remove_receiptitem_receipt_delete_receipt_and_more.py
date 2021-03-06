# Generated by Django 4.0 on 2021-12-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(default='null', max_length=80)),
                ('producto', models.CharField(default='null', max_length=80)),
                ('factura_fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de compra')),
                ('direccion_envio', models.CharField(default='null', max_length=80, verbose_name='Direccion de envío')),
                ('metodo_pago', models.CharField(default='null', max_length=20, verbose_name='Método de pago')),
                ('valor_envio', models.IntegerField(default='null', verbose_name='valor de envío')),
                ('valor_producto', models.IntegerField(default='null', verbose_name='valor de producto')),
                ('valor_impuesto', models.IntegerField(default='null', verbose_name='valor de impuesto')),
                ('subtotal', models.IntegerField(default='null', verbose_name='Subtotal')),
                ('valor_total', models.IntegerField(default='null', verbose_name='valor total')),
            ],
        ),
        migrations.RemoveField(
            model_name='receiptitem',
            name='receipt',
        ),
        migrations.DeleteModel(
            name='Receipt',
        ),
        migrations.DeleteModel(
            name='ReceiptItem',
        ),
    ]
