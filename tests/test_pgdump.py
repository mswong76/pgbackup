import pytest
import subprocess
from pgbackup import pgdump

url = "postgres://username:password@hostname:port/db_name"

def test_dump_call_pgdump(mocker):
	"""
	Utilize pg_dump to interact with Database.
	"""
	proc = mocker.Mock()
	mocker.patch('subprocess.Popen', return_value=proc)
	assert pgdump.dump(url)
	# calling subprocess.Popen with the following parameters
	subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
	"""
	pgdump.dump returns a reasonalbe error if pg_dump isn't installed
	"""
	mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
	with pytest.raises(SystemExit):
		pgdump.dump(url)