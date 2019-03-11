# Generated by Django 2.1.7 on 2019-03-09 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.BaseModel')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='key')),
                ('count', models.IntegerField(default=0, verbose_name='count')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.AlterUniqueTogether(
            name='counter',
            unique_together={('key', 'owner')},
        ),
    ]