# Generated by Django 4.1.1 on 2022-09-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=30)),
                ('tutorial_content', models.TextField()),
                ('tutorial_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
