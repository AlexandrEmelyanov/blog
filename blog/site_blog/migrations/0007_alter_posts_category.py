# Generated by Django 4.2.3 on 2023-08-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_blog', '0006_postcategory_post_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(default='Разное', on_delete=django.db.models.deletion.CASCADE, to='site_blog.postcategory'),
        ),
    ]
