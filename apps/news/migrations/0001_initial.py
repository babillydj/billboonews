# Generated by Django 2.1.1 on 2018-09-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('deleted', 'Deleted')], default='draft', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('topics', models.ManyToManyField(to='topics.Topics')),
            ],
        ),
    ]