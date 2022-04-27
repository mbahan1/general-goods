# Generated by Django 4.0.3 on 2022-04-23 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Dawnstar', 'Dawnstar'), ('Falkreath', 'Falkreath'), ('Markarth', 'Markarth'), ('Morthal', 'Morthal'), ('Riften', 'Riften'), ('Solitude', 'Solitude'), ('Whiterun', 'Whiterun'), ('Winterhold', 'Winterhold'), ('Windhelm', 'Windhelm')], max_length=50)),
                ('avatar', models.CharField(choices=[('Altmer', 'Altmer'), ('Argonian', 'Argonian'), ('Bosmer', 'Bosmer'), ('Breton', 'Breton'), ('Dunmer', 'Dunmer'), ('Imperial', 'Imperial'), ('Khajiit', 'Khajiit'), ('Nord', 'Nord'), ('Orsimer', 'Orsimer'), ('Redguard', 'Redguard'), ('...', '...')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bag',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=1),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='main_app.orderitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer'),
        ),
    ]
