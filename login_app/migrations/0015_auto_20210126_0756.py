# Generated by Django 3.1.4 on 2021-01-26 13:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0014_auto_20210125_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='last_edited_on',
            field=models.DateField(default=datetime.datetime(2021, 1, 26, 13, 56, 34, 243133, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='login_app.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='login_app.user')),
            ],
        ),
    ]
