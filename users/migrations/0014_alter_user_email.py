# Generated by Django 4.1.7 on 2023-02-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0013_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
