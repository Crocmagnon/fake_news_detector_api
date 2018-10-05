# Generated by Django 2.1.2 on 2018-10-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('domain_score', models.PositiveIntegerField(blank=True, null=True)),
                ('author_score', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
