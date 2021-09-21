# Generated by Django 3.1.7 on 2021-09-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='presioSupermonedas',
            new_name='precioSupermonedas',
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productos',
            name='codigoQR',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='efectivo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='marca',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productos',
            name='nombre',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precioNormal',
            field=models.FloatField(),
        ),
    ]
