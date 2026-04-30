#!/usr/bin/env python3
import re
import os

# Subject links from CSV
subject_links = {
    'digital technology': 'https://www.bbc.co.uk/bitesize/subjects/z9qy6yc',
    'chemistry': 'https://www.bbc.co.uk/bitesize/examspecs/zdycpg8',
    'english lang': 'https://www.bbc.co.uk/bitesize/examspecs/z3s43k7',
    'literature': 'https://www.bbc.co.uk/bitesize/examspecs/z8c7sg8',
    'french': 'https://www.bbc.co.uk/bitesize/examspecs/zmshxbk',
    'maths': 'https://www.bbc.co.uk/bitesize/examspecs/zcq8b82',
    'physics': 'https://www.bbc.co.uk/bitesize/examspecs/znjwvk7',
    'spanish': 'https://www.bbc.co.uk/bitesize/examspecs/zr2rydm',
    'biology': 'https://www.bbc.co.uk/bitesize/examspecs/zyqmv4j',
    'business': 'https://www.bbc.co.uk/bitesize/examspecs/z3969ty',
    'design and technology': 'https://www.bbc.co.uk/bitesize/examspecs/zvvwvj6',
    'geography': 'https://www.bbc.co.uk/bitesize/examspecs/zyp7jty',
    'history': 'https://www.bbc.co.uk/bitesize/examspecs/z3b4v9q',
    'learning for life and work': 'https://www.bbc.co.uk/bitesize/subjects/zq9xdxs',
    'media studies': 'https://www.bbc.co.uk/bitesize/subjects/ztnygk7',
    'religious': 'https://www.bbc.co.uk/bitesize/examspecs/zm2s8xs'
}

def update_bbc_links_in_file(filename, updates):
    """Update BBC Bitesize links in a specific file"""
    if not os.path.exists(filename):
        print(f"File {filename} does not exist")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for subject_key, new_link in updates.items():
        # Pattern to find BBC Bitesize links
        pattern = r'(<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(" title="BBC Bitesize[^"]*">BBC Bitesize[^<]*</a>)'
        
        # Find all BBC Bitesize buttons in the file
        matches = re.finditer(pattern, content)
        
        # For files with multiple sections, we need to be more specific
        if filename == 'science.html':
            # Update specific sections based on subject
            if subject_key == 'biology':
                content = re.sub(
                    r'(<h2>Biology</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
            elif subject_key == 'chemistry':
                content = re.sub(
                    r'(<h2>Chemistry</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
            elif subject_key == 'physics':
                content = re.sub(
                    r'(<h2>Physics</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
        elif filename == 'english.html':
            if subject_key == 'english lang':
                content = re.sub(
                    r'(<h2>English Language</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
            elif subject_key == 'literature':
                content = re.sub(
                    r'(<h2>English Literature</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
        elif filename == 'maths.html':
            if subject_key == 'maths':
                content = re.sub(
                    r'(<h2>GCSE Maths</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
        elif filename == 'languages.html':
            if subject_key == 'french':
                content = re.sub(
                    r'(<h2>French</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
            elif subject_key == 'spanish':
                content = re.sub(
                    r'(<h2>Spanish</h2>.*?<a class="placeholder-button placeholder-button-secondary" href=")[^"]*(".*?>BBC Bitesize.*?</a>)',
                    f'\\1{new_link}\\2',
                    content,
                    flags=re.DOTALL
                )
        else:
            # For single-subject files, update all BBC Bitesize links
            content = re.sub(pattern, f'\\1{new_link}\\2', content)
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename}")

# File mappings
file_updates = {
    'science.html': {
        'biology': subject_links['biology'],
        'chemistry': subject_links['chemistry'],
        'physics': subject_links['physics']
    },
    'english.html': {
        'english lang': subject_links['english lang'],
        'literature': subject_links['literature']
    },
    'maths.html': {
        'maths': subject_links['maths']
    },
    'religious-studies.html': {
        'religious': subject_links['religious']
    },
    'business-studies.html': {
        'business': subject_links['business']
    },
    'digital-technology.html': {
        'digital technology': subject_links['digital technology']
    },
    'design-technology.html': {
        'design and technology': subject_links['design and technology']
    },
    'geography.html': {
        'geography': subject_links['geography']
    },
    'history.html': {
        'history': subject_links['history']
    },
    'media-studies.html': {
        'media studies': subject_links['media studies']
    },
    'languages.html': {
        'french': subject_links['french'],
        'spanish': subject_links['spanish']
    }
}

# Update all files
for filename, updates in file_updates.items():
    update_bbc_links_in_file(filename, updates)

print("BBC Bitesize link updates completed!")