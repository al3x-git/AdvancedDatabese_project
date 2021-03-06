# Generated by Django 3.0.5 on 2021-05-27 08:35

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreatedUpdated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialIssue',
            fields=[
                ('createdupdated_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.CreatedUpdated')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=myapp.models.uploads)),
                ('description', models.TextField()),
            ],
            bases=('myapp.createdupdated',),
        ),
    ]
