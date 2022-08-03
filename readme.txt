1. Download python from https://www.python.org/downloads/
Download python, saved to c:\temp
Open an admin PowerShell prompt
Run the command C:\temp\python-3.10.6-amd64.exe

2. Download Git for windows from:
https://git-scm.com/download/win
Install with default settings (next next next)

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


4. Install great expectations from here (if you don't need great_expctations - skip to next step)
https://docs.greatexpectations.io/docs/tutorials/getting_started/tutorial_setup


pip install great_expectations


5. pip install pytest

6. pip install pyclean

7. pip install pytest-html

8. pip install pyyaml

9. (optional) pip install pandas-profiling[notebook]

10. Install databricks-connect 
https://docs.databricks.com/dev-tools/databricks-connect.html


