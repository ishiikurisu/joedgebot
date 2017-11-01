make: test

bot:
	python bot.py $(API)

cli:
	echo "TODO Compile CLI application"

test: test_main test_cli
	
test_main:
	python test_main.py

test_cli: cli
	python test_cli.py
