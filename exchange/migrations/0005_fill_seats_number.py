import re

from django.db import migrations


def text_to_number(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        match = re.search(r"\d+", program.seats)  # шукає цифри (\d) (усі разом, бо +)
        if match is None:
            raise ValueError(f"Немає числа в значенні місць: {program.seats!r}")
        program.seats_number = int(match.group())
        program.save(update_fields=["seats_number"])


def number_to_text(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.seats = str(program.seats_number)
        program.save(update_fields=["seats"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0004_add_seats_number"),
    ]

    operations = [
        migrations.RunPython(text_to_number, reverse_code=number_to_text),
    ]