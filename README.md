### Install dependencies

`pip install -r requirements.txt`

### Authenticate in huggingface-hub using a token from huggingface.co/settings/tokens

`huggingface-cli login`

### Create `config.py` and fill env variables as in `example_config.py`

### Run `bot.py`

`python bot.py`

## Usage with Docker-compose:

### 1. Create `.env` and fill env variable as in `.env.example`

### 2. Run `docker-compose`:

`docker-compose up --build`
