from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]