# Generated by Django 4.1.3 on 2022-11-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bankstatement_alter_upload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Upload',
            new_name='BUpload',
        ),
        migrations.AlterField(
            model_name='bankstatement',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
