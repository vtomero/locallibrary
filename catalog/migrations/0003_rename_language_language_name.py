# Generated by Django 5.0.2 on 2024-03-24 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_language_book_language"),
    ]

    operations = [
        migrations.RenameField(
            model_name="language",
            old_name="Language",
            new_name="name",
        ),
    ]
