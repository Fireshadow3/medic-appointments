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
    * [ ] Lista pazienti
    * [ ] Dettaglio pazienti
    * [ ] Creazione appuntamento (paziente,medico,tipologia visita, giorno)
    * [ ] Ricerca appuntamenti per medico (da data - a data e per tipologia)
    * [ ] Ricerca appuntamenti per paziente (da data - a data e per tipologia)
    * [ ] Dettaglio appuntamento
    * [ ] Creazione visita da appuntamento
    * [ ] Lista visite per paziente (da data)
    * [ ] Dettaglio visita

Pannelli su django-admin:
* [ ] Gestione tipologie visite
* [ ] gestione medici (con una inline delle tipologie di visite erogabili dal medico)
    * many to many tipologie medici, che fa vedere quali tipologie può avere un medico
* [ ] Gestione pazienti (con una inline degli appuntamenti presi e delle visite ricevute)

Admin user:
python manage.py createsuperuser
User:
admin
Password:
testtest
