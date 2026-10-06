from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0005_fill_seats_number"),
    ]

    operations = [
        migrations.RemoveField(model_name="exchangeprogram", name="seats"),
        migrations.RenameField(
            model_name="exchangeprogram",
            old_name="seats_number",
            new_name="seats",
        ),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveSmallIntegerField("Кількість місць"),
        ),
    ]
