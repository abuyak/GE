1. Download Git for windows from:
https://git-scm.com/download/win

2. Install with default settings (next next next)

3. Add the following paths to PATH:

    C:\Program Files\Git\bin\
    C:\Program Files\Git\cmd\


Modifying PATH on Windows 10:

    In the Start Menu or taskbar search, search for "environment variable".
    Select "Edit the system environment variables".
    Click the "Environment Variables" button at the bottom.
    Double-click the "Path" entry under "System variables".
    With the "New" button in the PATH editor, add C:\Program Files\Git\bin\ and C:\Program Files\Git\cmd\ to the end of the list.
    Close and re-open your console (or restart IDE)


4. Setup great expectations from here
https://docs.greatexpectations.io/docs/tutorials/getting_started/tutorial_setup

5. Create new data source. When creating data source chose Pandas and set the path to the data as "data"
great_expectations datasource new

This Datasource does not require any credentials. However, if you were to connect to a database that requires
connection credentials, those would be stored in great_expectations/uncommitted/config_variables.yml.

In the future, you can modify or delete your configuration by editing your
great_expectations.yml and config_variables.yml files directly

==============
Create Expectations
===========

6. Create new suite
great_expectations suite new

7. Setup a checkpoint
great_expectations checkpoint new getting_started_checkpoint

8. pip install pandas-profiling[notebook]

9. pip install pytest

10. pip install pyclean
