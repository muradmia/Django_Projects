# Generated by Django 5.0.1 on 2024-10-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_input_d_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_model',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='post/media/uploads/'),
        ),
    ]
