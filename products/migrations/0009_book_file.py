# Generated by Django 4.2.16 on 2024-10-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_download_file_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default='path/to/default/file.txt', upload_to='uploads/'),
        ),
    ]
