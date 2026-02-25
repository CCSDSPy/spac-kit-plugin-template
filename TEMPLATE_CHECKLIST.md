# Template Customization Checklist

Use this checklist when setting up a new project from this template.

## 1. Project Metadata

- [ ] Update `pyproject.toml`:
  - [ ] Change `name = "spac-kit-your-mission"` to your mission name
  - [ ] Update `description`
  - [ ] Update `authors` with your name and email
  - [ ] Update `license` if needed
  - [ ] Verify Python version requirements

## 2. File Structure

- [ ] Rename directories:
  - [ ] `ccsds/packets/example_mission/` → `ccsds/packets/your_mission/`
  - [ ] `ccsds/packets/your_mission/example_instrument/` → `ccsds/packets/your_mission/your_instrument/`

- [ ] Rename Python files:
  - [ ] `example_packet.py` → `your_packet.py`
  - [ ] Update `__init__.py` imports to match new filenames

- [ ] Update test files:
  - [ ] Rename `test_example.py` → `test_your_instrument.py`
  - [ ] Update class names in test file

## 3. Packet Definitions

- [ ] Replace example packet fields with your actual ICD definitions:
  - [ ] Update field names
  - [ ] Update bit lengths
  - [ ] Update data types
  - [ ] Set correct APID values
  - [ ] Choose FixedLength or VariableLength packet type

- [ ] Create or update test data:
  - [ ] Replace or create `test/in.bin` with real or synthetic data
  - [ ] Delete `test/out.pickle` if it exists (will be regenerated)

## 4. Documentation

- [ ] Update `docs/conf.py`:
  - [ ] Change package name in `metadata = importlib.metadata.metadata("...")`
  - [ ] Update `spacdocs_packet_modules` list with your module paths

- [ ] Update `docs/index.rst`:
  - [ ] Replace title with your mission name
  - [ ] Add any custom documentation sections

- [ ] Update `README.md`:
  - [ ] Update title and badges
  - [ ] Add mission-specific information
  - [ ] Update repository URLs
  - [ ] Add any custom installation or usage instructions

## 5. GitHub Configuration

- [ ] Update repository settings:
  - [ ] Repository name
  - [ ] Description
  - [ ] Topics/tags

- [ ] Add GitHub Secrets (Settings → Secrets and variables → Actions):
  - [ ] `PYPI_TOKEN` - Your PyPI API token

- [ ] Add GitHub Variables (Settings → Secrets and variables → Actions):
  - [ ] `PYPI_REPOSITORY` - Repository name (e.g., `pypi` or `testpypi`)
  - [ ] `PYPI_REPOSITORY_URL` - Repository URL

- [ ] Enable GitHub Pages (Settings → Pages):
  - [ ] Source: GitHub Actions

## 6. Development Setup

- [ ] Create and activate virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  ```

- [ ] Install dependencies:
  ```bash
  pip install -e '.[dev]'
  # OR
  poetry install --extras dev
  ```

- [ ] Install pre-commit hooks:
  ```bash
  pre-commit install && pre-commit install -t pre-push
  ```

## 7. Testing

- [ ] Run initial tests:
  ```bash
  pytest -v
  ```

- [ ] Verify test output:
  - [ ] `out.pickle` is generated
  - [ ] All tests pass

- [ ] Run linters:
  ```bash
  flake8 ccsds
  pylint ccsds
  ```

## 8. Version Control

- [ ] Initialize git repository:
  ```bash
  git init
  git add .
  git commit -m "Initial commit from template"
  ```

- [ ] Push to GitHub:
  ```bash
  git remote add origin https://github.com/your-org/your-project.git
  git push -u origin main
  ```

## 9. Additional Files (Optional)

- [ ] Update or create `CODE_OF_CONDUCT.md`
- [ ] Update `LICENSE` with your organization's license
- [ ] Add `.zenodo.json` for DOI generation (see Europa Clipper example)
- [ ] Add any mission-specific documentation

## 10. Cleanup

- [ ] Delete this checklist file (`TEMPLATE_CHECKLIST.md`) when done
- [ ] Remove example files if no longer needed
- [ ] Update `QUICKSTART.md` with any project-specific steps

## Verification

After completing the checklist, verify:

- [ ] `pytest` passes all tests
- [ ] `flake8 ccsds` shows no errors
- [ ] `pylint ccsds` shows acceptable warnings
- [ ] Documentation builds: `cd docs && sphinx-build -b html . _build/html`
- [ ] Pre-commit hooks work: `git commit --allow-empty -m "Test hooks"`
- [ ] GitHub Actions workflow runs successfully (push to trigger)

## Next Steps

1. Add more packet definitions for additional APIDs
2. Create comprehensive test coverage
3. Document any custom data types or converters
4. Set up your first release (see README.md → Releasing section)

---

**Note**: Keep this checklist until your project is fully set up, then delete it.
