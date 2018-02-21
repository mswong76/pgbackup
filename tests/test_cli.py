import pytest

from pgbackup import cli

url = "postgres://username:password/db_name"

def test_parser_without_driver():
	"""
	Without a specified driver the parser will exit
	"""
	parser = cli.create_parser()
	with pytest.raises(SystemExit):
		parser.parse_args([url])

def test_parser_with_driver():
	"""
	The parser will exit if it recives a driver without a destination
	"""
	parser = cli.create_parser()
	with pytest.raises(SystemExit):
		parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination():
	"""
	The parser will not exit if it receives a drvier and destination
	"""
	parser = cli.create_parser()
	args = parser.parse_args([url, '--driver', 'local', '/some/path'])

	assert args.driver == 'local'
	assert args.destination == '/some/path'