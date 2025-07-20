# Zenodo Upload Guide

## Pre-Upload Checklist

### ✅ Files to Include
- [x] `README.md` - Main documentation
- [x] `LICENSE` - CC BY-NC 4.0 license
- [x] `VERSION` - Version tracking
- [x] `zenodo.json` - Metadata file
- [x] `manuscript/` - Complete LaTeX source and PDF
- [x] `src/` - All Python implementation scripts
- [x] `figures/` - Generated publication-quality figures
- [x] `results/` - Validation and analysis results
- [x] `EXECUTION_GUIDE.md` - Setup and execution instructions
- [x] `verify_execution.py` - Execution verification script

### ✅ Files to Exclude
- [x] `.DS_Store` - macOS system files
- [x] `venv/` - Python virtual environment
- [x] `__pycache__/` - Python cache files
- [x] `*.pyc` - Compiled Python files
- [x] `.git/` - Git repository data

## Upload Steps

### 1. Prepare Archive
```bash
# Create clean archive excluding unnecessary files
tar -czf wavelength-field-theory-v1.0.0.tar.gz \
  --exclude='.DS_Store' \
  --exclude='venv' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.git' \
  .
```

### 2. Zenodo Upload Process

1. **Go to [Zenodo.org](https://zenodo.org)**
2. **Sign in** with your ORCID account
3. **Click "New Upload"**
4. **Drag and drop** your archive file
5. **Fill in metadata** (or use the provided `zenodo.json`)

### 3. Required Metadata Fields

#### Basic Information
- **Title**: "Beyond Einstein: A Complete Unified Field Theory from Wavelength Addition Principles"
- **Authors**: Oliver Jay Hooton (ORCID: 0009-0009-8775-1838)
- **Description**: Use the description from `zenodo.json`
- **Keywords**: Use the keywords from `zenodo.json`

#### Upload Type
- **Upload Type**: Publication
- **Publication Type**: Preprint
- **License**: Creative Commons Attribution-NonCommercial 4.0 International

#### Communities
- Add to "Theoretical Physics" community
- Add to "Quantum Physics" community

#### References
Include key references:
- MICROSCOPE Collaboration (2022)
- LIGO Scientific Collaboration (2016)
- Planck Collaboration (2020)

### 4. Post-Upload Tasks

#### Update DOI References
After upload, you'll receive a DOI like `10.5281/zenodo.1234567`. Update these files:

1. **README.md**: Replace `XXXXXXX` with your actual DOI
2. **zenodo.json**: Update the DOI in related_identifiers
3. **Citation**: Update the BibTeX citation with the correct DOI

#### Update Badges
Replace the placeholder DOI badge in README.md:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.YOUR_ACTUAL_DOI.svg)](https://doi.org/10.5281/zenodo.YOUR_ACTUAL_DOI)
```

## Version Management

### For Future Updates
1. **Increment version** in `VERSION` file
2. **Update** `zenodo.json` with new version
3. **Create new archive** with version number
4. **Upload as new version** on Zenodo

### Version Naming Convention
- `v1.0.0` - Initial release
- `v1.0.1` - Bug fixes
- `v1.1.0` - New features
- `v2.0.0` - Major changes

## Important Notes

### License Compatibility
- ✅ CC BY-NC 4.0 is fully compatible with Zenodo
- ✅ Allows academic use and citation
- ✅ Prevents commercial exploitation

### Citation Impact
- Zenodo provides persistent DOIs
- Enables proper academic citation
- Integrates with citation databases

### Long-term Preservation
- Zenodo provides long-term archival
- Multiple backup locations
- Version control for updates

## Troubleshooting

### Common Issues
1. **File too large**: Exclude `venv/` and other large directories
2. **Metadata errors**: Use the provided `zenodo.json` template
3. **DOI not working**: Wait 24-48 hours for DOI activation

### Support
- Zenodo Help: https://help.zenodo.org/
- ORCID Support: https://support.orcid.org/
- GitHub Issues: https://github.com/oliverjay/wavelength-addition/issues 