# Generated by Django 5.1.4 on 2024-12-16 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complate', models.BooleanField(default=False)),
                ('post', models.BooleanField(default=False)),
                ('delete', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.BigIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(default='-', max_length=15)),
                ('is_bot', models.BooleanField(default=False)),
                ('language_code', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Joined')),
                ('step', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=100)),
                ('telegraph', models.URLField(default='https://telegra.ph/file/6529587f8e3bd7a9b0c56.jpg')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='bot.car')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('currnet_page', models.IntegerField(default=1)),
                ('complate', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.tguser')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='dislikes',
            field=models.ManyToManyField(related_name='disliked_cars', to='bot.tguser'),
        ),
        migrations.AddField(
            model_name='car',
            name='likes',
            field=models.ManyToManyField(related_name='liked_cars', to='bot.tguser'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.tguser'),
        ),
        migrations.AddField(
            model_name='car',
            name='seen',
            field=models.ManyToManyField(related_name='seen_cars', to='bot.tguser'),
        ),
    ]
