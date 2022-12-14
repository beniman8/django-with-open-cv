# Generated by Django 4.1.2 on 2022-10-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opencv_site", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="upload",
            name="action",
            field=models.CharField(
                choices=[
                    ("NO_FILTER", "no filter"),
                    ("COLORIZED", "colorized"),
                    ("GRAYSCALE", "grayscale"),
                    ("BLURRED", "blurred"),
                    ("BINARY", "binary"),
                    ("INVERT", "invert"),
                ],
                max_length=50,
            ),
        ),
    ]
