# Generated by Django 4.1.2 on 2022-10-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrImage', models.ImageField(blank=True, null=True, upload_to='Upscale/image')),
            ],
        ),
    ]
