#!/bin/bash
# 741 Website Build System - Deploy Script

echo "Checking project status..."
git status

echo "Adding changes..."
git add -A

echo "Committing End-of-Day Backup..."
git commit -m "chore: end-of-day backup and section update"

echo "Pushing to remote repository..."
git push origin main

echo "Deployment complete."
