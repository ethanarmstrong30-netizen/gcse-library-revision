#!/usr/bin/env python3
import csv
import os
import re
from pathlib import Path

# Parse the CSV data
csv_data = """Subject,link
Digital technology,https://www.bbc.co.uk/bitesize/subjects/z9qy6yc
Chemistry,https://www.bbc.co.uk/bitesize/examspecs/zdycpg8
English lang,https://www.bbc.co.uk/bitesize/examspecs/z3s43k7
literature,https://www.bbc.co.uk/bitesize/examspecs/z8c7sg8
french,https://www.bbc.co.uk/bitesize/examspecs/zmshxbk
maths,https://www.bbc.co.uk/bitesize/examspecs/zcq8b82
physics,https://www.bbc.co.uk/bitesize/examspecs/znjwvk7
spanish,https://www.bbc.co.uk/bitesize/examspecs/zr2rydm
biology,https://www.bbc.co.uk/bitesize/examspecs/zyqmv4j
business,https://www.bbc.co.uk/bitesize/examspecs/z3969ty
Design and Technology,https://www.bbc.co.uk/bitesize/examspecs/zvvwvj6
Geography,https://www.bbc.co.uk/bitesize/examspecs/zyp7jty
History,https://www.bbc.co.uk/bitesize/examspecs/z3b4v9q
Learning for life and work,https://www.bbc.co.uk/bitesize/subjects/zq9xdxs
Media studies,https://www.bbc.co.uk/bitesize/subjects/ztnygk7
Religious,https://www.bbc.co.uk/bitesize/examspecs/zm2s8xs"""

# Parse CSV data into dictionary
subject_links = {}
lines = csv_data.strip().split('\n')[1:]  # Skip header
for line in lines:
    parts = line.split(',', 1)
    if len(parts) == 2:
        subject = parts[0].strip().lower()
        link = parts[1].strip()
        subject_links[subject] = link

print("Subject links from CSV:")
for subject, link in subject_links.items():
    print(f"  {subject}: {link}")

# List existing HTML files
html_files = []
for file in os.listdir('.'):
    if file.endswith('.html') and file not in ['index.html', 'all-subjects.html', 'edtech.html']:
        html_files.append(file)

print(f"\nExisting HTML files: {html_files}")

# Create mapping of subjects to files
subject_to_file = {
    'biology': 'science.html',
    'chemistry': 'science.html', 
    'physics': 'science.html',
    'maths': 'maths.html',
    'english lang': 'english.html',
    'literature': 'english.html',
    'religious': 'religious-studies.html',
    'business': 'business-studies.html',
    'digital technology': 'digital-technology.html',
    'french': 'languages.html',
    'spanish': 'languages.html',
    'design and technology': 'design-technology.html',
    'geography': 'geography.html',
    'history': 'history.html',
    'media studies': 'media-studies.html'
}

# Check which subjects need new files
missing_files = []
for subject in subject_links.keys():
    if subject not in subject_to_file:
        missing_files.append(subject)

print(f"\nSubjects that need new HTML files: {missing_files}")
print(f"\nSubject to file mapping:")
for subject, file in subject_to_file.items():
    print(f"  {subject} -> {file}")