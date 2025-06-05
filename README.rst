
Notes
=====

Use of a
`virtual environment <https://docs.python.org/3/library/venv.html>`_
is strongly recommended::

   git clone https://github.com/randall-frank/mrt-source.git
   cd mrt-source
   pip install virtualenv
   python -m virtualenv venv
   .\venv\Scripts\activate.ps1   # for Windows PowerShell, different for other shells
   pip install -r requirements.txt


Build
~~~~~

For heresy::

   cd heresy
   pelican
   pelican --listen --port 9000


For mrtrashcan::

   cd mrtrashcan
   pelican
   pelican --listen --port 9000

For both::

   python build.py build
   python build.py serve heresy

----

Copyright (C) 2017-2025 Randall Frank