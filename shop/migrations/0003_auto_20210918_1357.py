# Generated by Django 3.2.4 on 2021-09-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210720_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
