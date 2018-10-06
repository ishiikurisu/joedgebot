make: cli

bot:
	python bot.py $(API)

cli:
	pyinstaller cli.py -F -n cli.exe
	mv dist/cli.exe .

test: test_main test_cli

test_main:
	python test_main.py

test_cli: cli
	python test_cli.py
	rm cli.exe
	rm *.class
