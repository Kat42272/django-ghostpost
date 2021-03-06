# Generated by Django 3.1 on 2020-08-20 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_roast', models.BooleanField()),
                ('body', models.CharField(max_length=280)),
                ('upVotes', models.IntegerField()),
                ('downVotes', models.IntegerField()),
                ('postDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
