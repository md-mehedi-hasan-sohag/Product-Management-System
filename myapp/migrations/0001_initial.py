# Generated by Django 5.0.4 on 2024-05-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='static/media/')),
            ],
        ),
    ]
