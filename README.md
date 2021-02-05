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

## License

Copyright 2021 Mauro Filipe Maia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.