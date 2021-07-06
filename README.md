## Description

Tool to encrypt PSKC files with a PBKDF2 passphrase, based on
[python-pskc](https://arthurdejong.org/python-pskc/).

## Usage

Start by installing [`pipenv`](https://pipenv.pypa.io/en/latest/).
```shell
# Linux/Windows
pip install pipenv

# macOS
brew install pipenv
```

Sync your environment.
```shell
pipenv sync
```

Now you can run the scripts with `pipenv`.
```shell
./pskc_encrypt.py pskc_plain.xml pskc_encrypted.xml
```

By default the tool will prompt you for a passphrase. You can use
`--passphrase` to specify a file containing the passphrase, or give it `-` to
use stdin.
