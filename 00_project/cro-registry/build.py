#!/usr/bin/env python3
"""Shim (2026-10-11): the Desktop Excel now covers all workflows. This script calls the new builder.
CRO pages stay in cro-registry/registry.json. Run: python3 00_project/cro-registry/build.py"""
import subprocess, sys
PY = '/Library/Frameworks/Python.framework/Versions/3.10/bin/python3'
sys.exit(subprocess.call([PY, '/Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py', 'build']))
