pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3

Preparing for Devlopment
------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github``
3. Fetch development dependencies ``make install``

Usage
-----

Pass in full database URL, the storage driver, and destination.

S3 Example w/ backet name:

::

    $ pgbackup postgres://db_username:password@hostname:port/db_name -- driver s3 backups

Local Example w/ local path:

::

    $ pgbackup postgres://db_username:password@hostname:port/db_name -- driver local /var/local/db_name/backups/db_name_dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active

::

    $ make

if virtualenv isn't active then use:

::

    $ pipenv run make
