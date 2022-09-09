# KijijiScraper
This project scrapes apartment rental announcements from kijiji.ca and saves collected results to the database. Tech stack: <br>
- Python3.9.12
- requests
- BeautifulSoup4
- SqlAlchemy
- PostgreSQL
## Dependencies 
The main one - you should have PostgreSQL installed on your machine to test this project.<br>
Project dependencies are listed within the `requirements.txt` file.
## Project installation and first launch
- Download the ZIP-file of the project.
- Set up the virtual environment: `python -m venv <YOUR_ENV_NAME>`
- Activate the virtual environment: `<YOUR_ENV_NAME>/scripts/activate`
- Install all dependencies: `pip install -r requirements.txt`
- Go to `db_conf.py` and replace arbitrary database credentials with those of your own working environment
- Run `create_db.py` script: `python create_db.py`
- Run `main.py` script: `python main.py`<br>
Since then, the project is ready. Each time `main.py` is activated, all `Announcement` rows are deleted. This is done to keep records unique and to prevent overpopulation of the database.
