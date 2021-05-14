Le entità da modellare sarebbero:

medici
pazienti
tipologia_appuntamenti
appuntamenti
visite

La visita è cosa viene fatto.
L'appuntamento può avere una sola visita.

Esponendo su admin i seguenti pannelli:

gestione tipologie visite
    Visita chirurgica, dentistica, altro
gestione medici (con una inline delle tipologie di visite erogabili dal medico)
    many to many tiplogie medici, che fa vedere quali tipologia può avere un emdico
gestione pazienti (con una inline degli appuntamenti presi e delle visite ricevute)


Riguardo le API REST da esporre:

EZ - lista medici
EZ - dettaglio medico
EZ - lista pazienti
EZ - dettaglio pazienti
MED - creazione appuntamento (paziente,medico,tipologia visita, giorno)
HARD - ricerca appuntamenti per medico (da data - a data e per tipologia)
HARD - ricerca appuntamenti per paziente (da data - a data e per tipologia)
EZ - dettaglio appuntamento
MED - creazione visita da appuntamento
MED - lista visite per paziente (da data)
EZ - dettaglio visita




