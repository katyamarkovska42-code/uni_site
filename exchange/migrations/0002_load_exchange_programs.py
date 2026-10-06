from django.db import migrations

# Дати записані у форматі РРРР-ММ-ДД, бо це внутрішній формат DateField.

INSERT_SQL = """
INSERT INTO exchange_exchangeprogram (university, languages, seats, deadline, description) VALUES
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
 'Найбільший університет Польщі з сильними програмами з біології та хімії.'),
('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
 'Один із найстаріших університетів Бельгії, відомий дослідженнями в галузі природничих наук.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
 'Найстаріший університет Литви з сучасними науковими лабораторіями.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
 'Краківський університет, заснований 1364 року, з сильною біологічною школою.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
 'Провідний університет Естонії, відомий програмами з екології та біотехнологій.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
 'Університет у місті Брно з великою природничою факультетською базою.');
"""


REVERSE_SQL = """
DELETE FROM exchange_exchangeprogram WHERE
  university LIKE 'Uniwersytet Warszawski%' OR
  university LIKE 'KU Leuven%' OR
  university LIKE 'Vilnius University%' OR
  university LIKE 'Uniwersytet Jagiello%' OR
  university LIKE 'University of Tartu%' OR
  university LIKE 'Masaryk University%';
"""


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(INSERT_SQL, reverse_sql=REVERSE_SQL),
    ]