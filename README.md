# shopic_test_assignment_backend

## Installation

1. run `pip install -r requirements.txt`
2. create `.env` file by example `.env.example`
3. generate secret key, and add it to `.env`
4. create postgresql database, and add name, user and password to `.env`
5. run `python manage.py migrate`
6. run `python manage.py load_data_from_url ...` for Items, then for Carts.
   1. `python manage.py load_data_from_url https://url.com/catalog.csv --format csv --model Item`
   2. `python manage.py load_data_from_url https://url.com/carts_big.json --format json --model Cart`
7. run `python manage.py runserver`