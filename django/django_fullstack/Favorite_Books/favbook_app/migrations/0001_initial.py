# Generated by Django 3.2.3 on 2021-05-30 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('passwod', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField(null=True, verbose_name='Date of Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_uploaded', to='favbook_app.user')),
                ('users_who_like', models.ManyToManyField(related_name='liked_books', to='favbook_app.User')),
            ],
        ),
    ]
