# Generated by Django 5.0 on 2024-02-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jeux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BibliothequeDeJeux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('jeux', models.ManyToManyField(blank=True, to='pysteamapp.jeux')),
            ],
        ),
    ]