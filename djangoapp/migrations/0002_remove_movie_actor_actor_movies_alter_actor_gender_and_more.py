# Generated by Django 4.1.3 on 2022-12-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangoapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="movie", name="actor",),
        migrations.AddField(
            model_name="actor",
            name="movies",
            field=models.ManyToManyField(to="djangoapp.movie"),
        ),
        migrations.AlterField(
            model_name="actor",
            name="gender",
            field=models.CharField(max_length=20, verbose_name="Gender"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genre",
            field=models.CharField(max_length=50, verbose_name="Genre"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="year",
            field=models.DateField(verbose_name="Relise_year"),
        ),
    ]
