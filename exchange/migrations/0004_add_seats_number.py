from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0003_split_university_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="seats_number",
            field=models.PositiveSmallIntegerField(null=True),
        ),

        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.CharField(max_length=50, blank=True, default=""),
        ),
    ]