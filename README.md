# Another password manager...

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run pwmanager cli application

$ pwmanager --help


### run pytest / coverage

$ make test
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
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `MFM Password Manager`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it pwmanager --help
```

## TODOS

- [ ] Create/Connect to storege only when required.
- [ ] At storage creation time set master user.
- [ ] Add option an option to save/replace a password
- [ ] Add a verification to force/list password entries with more than x time. 