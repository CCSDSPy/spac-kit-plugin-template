# SPaC-Kit Plugin Template

This is a template repository for creating CCSDS packet definition plugins for the [SPaC-kit library](https://github.com/CCSDSPy/SPAC-kit).

> [!IMPORTANT]
> **This library is currently in active development.**
>
> Some functions are placeholders and may not yet have full implementations. Expect ongoing updates and new features as the library evolves.

## What is this template for?

This template helps you quickly create a new Python package containing CCSDS packet definitions for your mission or instrument. These packet definitions are used by the SPaC-kit library to:
- Decode CCSDS packets from binary downlink files
- Generate comprehensive documentation for your packets
- Create simulated datasets for testing

## Getting Started

### Users

_(what you will get if you use this template for your packet definitions)_

The documentation of the packet is available on `http://<your org name>.github.io/<your repo name>` (TO BE UPDATED)

To use spac-kit tools with your packet definitions, you need:

- the packet definitions prepared from this repository template, in this case `spac-kit-your-mission`.
- the Spac-kit library
- Optionally one example data complying with the CCSDS Space Packet definitions available in this repository.

With traditional python environment:

    pip install spac-kit-your-mission  # the plugin prepared with your packet defintions from this template repository
    pip install spac-kit

Then see the list of packet definitions:

    spac-ls

```bash
APID  PACKET                                                                   NAME                   DESCRIPTION
-----------------------------------------------------------------------------------------------------------------
100   example_mission.example_instrument.example_packet.example_health_status  example_health_status
101   example_mission.example_instrument.metadata.metadata_example             example_metadata

```

Generate a dataset of 2 packets for the given definition, :

    spac-generate --apid 100 --count 2 --output file.out

(use `spac-generate` --help for more details)

Parse this data file:

    spac-parse --file file.dat



### Developers

#### 1. Use this template

Click the "Use this template" button on GitHub to create a new repository from this template, or clone this repository:

```bash
git clone <your-new-repo-url>
cd <your-new-repo-name>
```

#### 2. Customize the project

Update the following files with your mission/instrument information:

- **`pyproject.toml`**: Update the project name, description, version, and author information
- **`ccsds/packets/`**: Replace `example_mission` with your mission name
- **`docs/conf.py`**: Update the `spacdocs_packet_modules` list with your packet module paths

The system path must be preserved (`ccsds/packets/`) as it is used by the Spac-kit tools to discover your packet definitions.


#### 3. Set up your development environment

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

You might need to upgrade pip first:

```bash
pip install --upgrade pip
```

If you want to use the latest dev version of spac-kit, install it from the sources:

```bash
git clone https://github.com/CCSDSPy/SPaC-Kit.git
source {HOME OR PATH TO YOUR VENV}/bin/activate
pip install ./SPaC-Kit
```

Install the package in editable mode with developer dependencies:

```bash
pip install -e '.[dev]'
```

Or use poetry:

Install poetry from your local system (not in a virtual environment):

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH=${HOME}/.local/bin:${PATH}
```

Create a poetry virtual environment and install the package with developer dependencies:

```bash
poetry env use python3.12
poetry lock
poetry install --with dev
```

Optionally, to work with a local version of SPaC-Kit:

```bash
poetry add ../SPaC-Kit
```

**IMPORTANT**: Install the pre-commit hooks to ensure code quality. If you don't do this, the automated tests running on Pull Requests will fail:

```bash
pre-commit install && pre-commit install -t pre-push
```

Note: if you don't use poetry, you will need to replace the test configuration and remove the `poetry run` in the entry field.

#### 4. Define your CCSDS packets

Create your packet definitions in the `ccsds/packets/your_mission/your_instrument/` directory:

1. Create a new Python module for each packet type or instrument
2. Define packet structures using the [ccsdspy](https://docs.ccsdspy.org/en/latest/index.html) library, and for your packets, specifically, [`ccsdspy.FixedLength`](https://docs.ccsdspy.org/en/latest/user-guide/fixedlength.html#) or [`ccsdspy.VariableLength`](https://docs.ccsdspy.org/en/latest/user-guide/variablelength.html) objects.
3. Create test data files in a `test/` subdirectory alongside your packet definitions
4. Write unit tests to validate your packet parsing

See the example packet definition in `ccsds/packets/example_mission/example_instrument/` for reference.

#### 5. Create test data

For each packet definition, create corresponding test data:

- **`test/in.bin`**: Binary CCSDS packet data for testing
- **`test/out.pickle`**: Expected parsed output (generated by spac-kit after first successful parse)
- **`test/test_your_instrument.py`**: Unit test that uses `spac_kit.parser.compare()` to validate parsing

#### 6. Run tests

Run the tests to ensure everything is working:

```bash
pytest
```

or with poetry:

```bash
poetry run pytest
```


Before committing your changes, update the poetry lock file:

```bash
poetry lock
```

#### 7. Generate/Visualize documentation

The project uses Sphinx with the SPaC-kit autodocs extension to automatically generate documentation from your packet definitions.

To build and visualize the documentation locally:

```bash
cd docs
sphinx-build -b html . _build/html
```

(with poetry don't forget the `poetry run` prefix)

The generated documentation will be in `docs/_build/html/`.

To test the documentation and visualize it in a browser. you can use `sphinx-autobuild`:

```bash
pip install sphinx-autobuild
```

or with poetry:
```bash
poetry add sphinx-autobuild
```

And build-start the server:

    poetry run sphinx-autobuild -b html . _build/html



## Project Structure

```
.
├── .github/
│   └── workflows/
│       ├── ci.yml              # Linting and testing workflow
│       └── publish.yml         # PyPI publishing and docs deployment
├── ccsds/
│   └── packets/
│       └── example_mission/    # Replace with your mission name
│           └── example_instrument/  # Your instrument name
│               ├── __init__.py
│               ├── metadata.py      # Packet metadata
│               ├── example_packet.py  # Packet definitions
│               └── test/
│                   ├── __init__.py
│                   ├── in.bin       # Test binary data
│                   ├── out.pickle   # Expected output
│                   └── test_example.py  # Unit tests
├── docs/
│   ├── conf.py                 # Sphinx configuration
│   ├── index.rst               # Documentation index
│   └── _static/                # Static files for docs
├── .flake8                     # Flake8 linting config
├── .gitignore                  # Git ignore patterns
├── .pre-commit-config.yaml     # Pre-commit hooks config
├── pyproject.toml              # Project metadata and dependencies
└── README.md                   # This file
```

## Workflow

### Development workflow

1. Create a new branch for your changes
2. Add or modify packet definitions in `ccsds/packets/`
3. Create/update test data in the `test/` directories
4. Run tests locally with `pytest`
5. Commit your changes (pre-commit hooks will run automatically)
6. Push your branch and create a Pull Request


### CI/CD Pipeline

The template includes two GitHub Actions workflows:

#### 1. Lint, Test, and Release (`ci.yml`)

Runs on pushes to `main` and Pull Requests:
- Lints code with `flake8` and `pylint`
- Runs all unit tests with `pytest`
- Creates a GitHub release when PRs are merged (if configured)

#### 2. Publish to PyPI (`publish.yml`)

Runs on release branches and published releases:
- Publishes to PyPI Test when pushing to `release/*` branches
- Publishes to PyPI Production when a release is published on GitHub
- Builds and deploys documentation to GitHub Pages

### Releasing

To prepare for a new release:

1. Create a release branch:
```bash
git checkout -b release/X.Y.Z
git push
```

2. This automatically publishes to PyPI Test environment for testing

3. Create a Pull Request to merge the release branch into `main`

4. Once merged, the workflow will:
   - Create a git tag
   - Create a GitHub release
   - Publish to PyPI
   - Deploy documentation to GitHub Pages

## GitHub Configuration

To enable all features, configure the following in your GitHub repository:

### Secrets

- `PYPI_TOKEN`: PyPI API token for publishing packages

### Variables

- `PYPI_REPOSITORY`: Repository name (e.g., `pypi` for production, `testpypi` for test)
- `PYPI_REPOSITORY_URL`: Repository URL (e.g., `https://upload.pypi.org/legacy/` or `https://test.pypi.org/legacy/`)

### GitHub Pages

Enable GitHub Pages in repository settings:
- Source: GitHub Actions
- This allows the `publish.yml` workflow to deploy documentation

## Support

For issues or questions:
- SPaC-kit library: https://github.com/CCSDSPy/SPAC-kit
- CCSDS packet definitions: Refer to your mission's ICD documents

## License

Update the license in `pyproject.toml` according to your organization's requirements.
