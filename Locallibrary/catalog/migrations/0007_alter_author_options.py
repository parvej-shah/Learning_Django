# Generated by Django 4.0 on 2022-02-11 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_add_author', 'Can add author'), ('can_delete_author', 'Can delete author'), ('can_update_author', 'Can update author'))},
        ),
    ]