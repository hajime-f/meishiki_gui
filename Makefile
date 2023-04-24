all:
	python3 meishiki_gui.py $(BIRTH) $(SEX)
install:
	pip install -r requirements.txt
