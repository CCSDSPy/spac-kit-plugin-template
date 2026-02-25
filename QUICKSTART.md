# Quick Start Guide

This guide will help you quickly set up and customize this template for your CCSDS packet definitions project.

## 1. Initial Setup (5 minutes)

### Clone or use this template

```bash
# If using GitHub's "Use this template" button, clone your new repo:
git clone https://github.com/your-org/your-project.git
cd your-project

# Or if you downloaded this as a template:
cd spac-kit-plugin-template
```

### Update project metadata

Edit `pyproject.toml` and replace:
- `name = "spac-kit-your-mission"` → your mission name
- `description = "..."` → your description
- `authors = [...]` → your information

## 2. Rename Example Files (5 minutes)

### Rename the mission directory

```bash
cd ccsds/packets/
mv example_mission your_mission_name
cd your_mission_name
mv example_instrument your_instrument_name
cd ../../..
```

### Update imports

Edit `ccsds/packets/your_mission_name/your_instrument_name/__init__.py`:
```python
from .your_packet import your_packet_name  # noqa
from .metadata import metadata_your_instrument  # noqa
```

## 3. Define Your First Packet (15 minutes)

### Study your ICD (Interface Control Document)

Identify:
- APID (Application Process Identifier)
- Packet fields and their bit lengths
- Data types (uint, int, float)
- Field names

### Edit example_packet.py

Replace the example fields with your actual packet structure based on your ICD.

Example:
```python
my_packet_fields = [
    # CCSDS Primary Header (standard)
    ccsdspy.PacketField(name="CCSDS_VERSION", bit_length=3, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_TYPE", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEC_HDR_FLG", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_APID", bit_length=11, data_type="uint"),
    # ... add your fields here
]

my_packet = ccsdspy.VariableLength(my_packet_fields)
my_packet.name = "my_packet_name"
my_packet.apid = 123  # Your APID
```

## 4. Create Test Data (10 minutes)

### Option A: Use real data

If you have actual binary CCSDS data:
```bash
cp /path/to/your/data.bin ccsds/packets/your_mission/your_instrument/test/in.bin
```

### Option B: Create synthetic data

Use Python's `struct` module to create a binary packet matching your definition.

## 5. Test Your Packet Definition (5 minutes)

### Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e '.[dev]'
```

### Run tests

```bash
# First run will create the reference output file
pytest -v
```

If the test passes, a `out.pickle` file will be created in the test directory.

## 6. Set Up Documentation (5 minutes)

### Update docs configuration

Edit `docs/conf.py` and update:
```python
metadata = importlib.metadata.metadata("spac-kit-your-mission")  # Your package name
spacdocs_packet_modules = [
    'ccsds.packets.your_mission.your_instrument',  # Your module path
]
```

### Build documentation locally (optional)

```bash
cd docs
sphinx-build -b html . _build/html
# Open _build/html/index.html in your browser
```

## 7. Set Up Git and CI/CD (10 minutes)

### Initialize git repository

```bash
git init
git add .
git commit -m "Initial commit: Set up CCSDS packet definitions template"
```

### Push to GitHub

```bash
git remote add origin https://github.com/your-org/your-project.git
git push -u origin main
```

### Configure GitHub repository

In your GitHub repository settings:

1. **Secrets and Variables** → **Actions** → **Secrets**:
   - Add `PYPI_TOKEN` (get from https://pypi.org/manage/account/token/)

2. **Secrets and Variables** → **Actions** → **Variables**:
   - Add `PYPI_REPOSITORY`: `pypi` (or `testpypi` for testing)
   - Add `PYPI_REPOSITORY_URL`: `https://upload.pypi.org/legacy/`

3. **Settings** → **Pages**:
   - Source: **GitHub Actions**

### Install pre-commit hooks

```bash
pre-commit install && pre-commit install -t pre-push
```

## Next Steps

- Add more packet definitions for other APIDs
- Create comprehensive test data
- Document any custom converters or special handling
- Set up your first release

## Common Issues

### Tests fail with "Module not found"

Make sure you've installed the package in editable mode:
```bash
pip install -e '.[dev]'
```

### Import errors

Check that all `__init__.py` files are present and have correct imports.

### Binary test data doesn't parse

Verify your packet field definitions match your ICD exactly, paying attention to:
- Bit lengths
- Byte order (big-endian for CCSDS)
- Data types (signed vs unsigned)

## Getting Help

- SPaC-kit documentation: https://github.com/CCSDSPy/SPAC-kit
- ccsdspy documentation: https://ccsdspy.readthedocs.io/
- Open an issue in your repository for project-specific questions
