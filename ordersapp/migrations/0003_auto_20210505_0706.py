# Generated by Django 3.2.1 on 2021-05-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PRO', 'обработан'), ('PD', 'оплачен'), ('RDY', 'готов к выдаче'), ('CNC', 'отменен')], db_index=True, default='FM', max_length=3, verbose_name='статус'),
        ),
    ]
