# Generated by Django 4.0.6 on 2022-07-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_slug_alter_product_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.CharField(choices=[('non defined', 'Non defined'), ('rock', 'Rock'), ('synth_wave', 'Synth wave'), ('post_punk', 'Post punk'), ('heavy_metal', 'Heavy metal')], default='non defined', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]