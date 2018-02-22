import tempfile
from pgbackup import storage

def test_storing_file_locally():
	"""
	Write content from one file-like to another
	"""
	infile = tempfile.TemporaryFile('r+')
	infile.write('Testing')
	infile.seek(0)

	outfile = tempfile.NamedTemporaryFile(delete=False)
	storage.local(infile, outfile)
	with open(outfile.name) as file:
		assert file.read() == 'Testing'