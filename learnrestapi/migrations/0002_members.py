# Generated by Django 4.2 on 2024-03-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnrestapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
            ],
        ),
    ]