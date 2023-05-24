# Lead Validator

Copy `websites.template.txt` to `websites.txt`

```sh
$ cp websites.template.txt websites.txt
```

Enable virtual environment for python and run script

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

It will generate invalid.txt with invalid entries.