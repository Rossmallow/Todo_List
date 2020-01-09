# Generated by Django 2.2.7 on 2020-01-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('comments', models.TextField()),
                ('due_date', models.DateField(default='2020-01-01')),
                ('star', models.BooleanField()),
            ],
        ),
    ]