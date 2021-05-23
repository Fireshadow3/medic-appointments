
This is a test project using the Django web framework.

For the list of TODOs, see TODO.md

For a list of documentation consulted while making this project, see links.txt

Structure of the project:

medicmodels/
    App containing all the models related to the medics and their appointments, as well as the patients models
medicapis/
    App that contains all of the requested APIs based on medicmodels models
medicadmin/
    App holding the requested django-admin views, as well as the views for all the other models in medicmodels
    
The rest of the project follows the standard layout structure.

A test sqlite database can be found in the root of the project, "db.sqlite3".
The default superuser to login into admin is "admin", with password "testtest"
