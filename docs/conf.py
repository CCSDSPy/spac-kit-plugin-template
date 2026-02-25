"""Sphinx configuration for documentation generation."""
import importlib.metadata

# Project information
# Update the package name to match your pyproject.toml
metadata = importlib.metadata.metadata("spac-kit-your-mission")
project = metadata["Name"]
author = metadata["Author"]
release = metadata["Version"]


extensions = [
    'spac_kit.autodocs',
    'sphinx_rtd_theme',
]

# Use Read the Docs theme for better sidebar navigation
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,  # Show up to 4 levels in sidebar
    'collapse_navigation': False,  # Keep sidebar expanded
}

# List of modules to scan for _BasePacket instances for documentation generation
# Update this list with your actual packet modules
spacdocs_packet_modules = [
    'ccsds.packets.example_mission.example_instrument',
]
