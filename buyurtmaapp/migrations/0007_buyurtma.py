# Generated by Django 4.1.3 on 2023-02-21 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_remove_profil_davlat'),
        ('buyurtmaapp', '0006_savat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('umumiy', models.PositiveIntegerField()),
                ('yetkazish', models.PositiveIntegerField(default=5)),
                ('yakuniy', models.PositiveIntegerField()),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
                ('savat', models.ManyToManyField(to='buyurtmaapp.savat')),
            ],
        ),
    ]