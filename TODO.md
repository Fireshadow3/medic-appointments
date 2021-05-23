## TODOs

* Modellare le entità
    * Medici
    * Pazienti
    * Tipologia_appuntamenti
    * Appuntamenti
    * Visite

Note:
La visita è cosa viene fatto durante un appuntamento.
L'appuntamento può avere una sola visita.

* API REST da esporre:
    * [X] Lista medici
    * [X] Dettaglio medico
    * [X] Lista pazienti
    * [X] Dettaglio pazienti
    * [X] Creazione appuntamento (paziente,medico,tipologia visita, giorno)
    * [X] Ricerca appuntamenti per medico (da data - a data e per tipologia)
    * [X] Ricerca appuntamenti per paziente (da data - a data e per tipologia)
    * [X] Dettaglio appuntamento
    * [X] Creazione visita da appuntamento
    * [X] Lista visite per paziente (da data)
    * [X] Dettaglio visita

Pannelli su django-admin:
* [X] Gestione tipologie visite
* [X] gestione medici (con una inline delle tipologie di visite erogabili dal medico)
    * many to many tipologie medici, che fa vedere quali tipologie può avere un medico
* [X] Gestione pazienti (con una inline degli appuntamenti presi e delle visite ricevute)

Admin user:
python manage.py createsuperuser
User:
admin
Password:
testtest
