# Generated by Django 2.2.5 on 2019-09-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attndance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emplyees',
            name='image',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
