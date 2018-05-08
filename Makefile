
run:
	FLASK_APP=LanguageSparksSite.py \
	FLASK_DEBUG=1 \
	flask run

update-requirements:
	pip freeze > requirements.txt

install-requirements:
	pip install -r requirements.txt
