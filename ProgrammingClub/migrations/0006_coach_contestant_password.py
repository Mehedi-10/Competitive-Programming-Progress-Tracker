# Generated by Django 4.1.5 on 2023-03-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammingClub', '0005_contestant_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_email', models.EmailField(blank=True, default=None, max_length=400, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contestant',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
