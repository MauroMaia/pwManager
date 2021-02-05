# Another password manager...

## Installation

```Bash
pip install -r requirements.txt

pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```Bash
### create a virtualenv for development

make virtualenv

source env/bin/activate


### run pwmanager cli application

pwmanager --help


### run pytest / coverage

make test
```

### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
make dist

make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `MFM Password Manager`, and can be built with the
included `make` helper:

```Bash
make docker

docker run -it pwmanager --help
```

## TODOS

- [ ] Create/Connect to storage only when required.
- [ ] At storage creation time set master user.
- [x] Add option an option to save a password
- [ ] Add an import option to load passwords from csv kdbx file
- [ ] Add option an option to replace a password
- [ ] Add option an option if set to show a time based warning to replace to generate a new password
- [ ] Remove database specific types to allow view/controller layer to integrate with other storage types.
