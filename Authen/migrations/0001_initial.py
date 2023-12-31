# Generated by Django 4.2.2 on 2023-08-09 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('Anambra', 'Anambra'), ('Delta', 'Delta'), ('Enugu', 'Enugu'), ('Edo', 'Edo'), ('Imo', 'Imo'), ('Abia', 'Abia'), ('Enonyi', 'Ebonyi'), ('Ogun', 'Ogun')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
