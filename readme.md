# Massagestudio

## User Story
Ein Massageinstitut vergibt Termine.
Zu jedem Termin kann man einen Masseur, einen Patienten, einen Raum und eine Behandlungsart hinzubuchen.


## Technische Spezifikation
Die Datenbank Massageinstitut enthält die Tabellen Zeitraster, Masseure, Patienten, Räume, Behandlungsart und Termine.

In der Tabelle Zeitraster sind die möglichen Beginnzeiten der Termine in 15 Minuten Schritten von 6:00 Uhr bis 20:00 Uhr eingetragen.
In der Tabelle Masseure befinden sich die Daten der praktizierenden Masseure.
In der Tabelle Patienten befinden sich die Daten der Kunden.
In der Tabelle Behandlungsart befinden sich die möglichen Behandlungsarten und Behandlungsdauern.
In der Tabelle Termine sind die gebuchten Termine, bestehend aus Beginnzeit, Dauer, Raum, Masseur, Kunde und Behandlungsart eingetragen.

Eine Benutzerverwaltung mit Zugriffsrechten ist ebenso wie eine Kostenabrechnung angedacht, soll im Moment aber noch nicht umgesetzt werden, in einem zukünftigen Auftrag aber eingebaut werden!

Erstellen Sie ein ER-Diagramm der Datenbank und setzen Sie dieses um (PostgreSQL).
Überlegen Sie sich die möglichen Abläufe und fertigen Sie jeweils ein Ablaufdiagramm an.
Erstellen Sie eine tkinter-Oberfläche mit der notwendigen CRUD-Funktionalität.
Überlegen Sie sich dazu die notwendige Klassenhierarchie und fertigen Sie ein Klassendiagramm an.

Setzen Sie für die Entwicklung einen Docker-Container auf und implementieren Sie das Projekt.