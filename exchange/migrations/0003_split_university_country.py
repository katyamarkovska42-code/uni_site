from django.db import migrations, models


def split_university(value):
    if value.endswith(")") and " (" in value:
        name, country = value[:-1].rsplit(" (", 1)
    elif " - " in value:
        name, country = value.rsplit(" - ", 1)
    elif ", " in value:
        name, country = value.rsplit(", ", 1)
    else:
        return value.strip(), ""
    return name.strip(), country.strip()


def split_name_and_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        name, country = split_university(program.university)
        program.university = name
        program.country = country
        program.save(update_fields=["university", "country"])


def join_name_and_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        if program.country:
            program.university = f"{program.university}, {program.country}"
            program.save(update_fields=["university"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0002_load_exchange_programs"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(default="", max_length=100, verbose_name="Країна"),
        ),
        migrations.RunPython(split_name_and_country, reverse_code=join_name_and_country),
    ]

