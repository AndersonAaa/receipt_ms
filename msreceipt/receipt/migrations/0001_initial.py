# Generated by Django 4.0 on 2021-12-09 22:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seller', models.CharField(max_length=120, verbose_name='seller name')),
                ('buyer', models.CharField(max_length=255, verbose_name='buyer name')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='auth.user')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service', models.CharField(max_length=255)),
                ('unit', models.CharField(help_text='Unit of measurement.', max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='unit rate')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='receipt.receipt')),
            ],
            options={
                'verbose_name': 'Receipt Item',
                'verbose_name_plural': 'Receipt Items',
            },
        ),
    ]
