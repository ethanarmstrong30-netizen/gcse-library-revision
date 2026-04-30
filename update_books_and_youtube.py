#!/usr/bin/env python3
import re
import os

# Parse book data from both CSV files
general_books_data = """Barcode,Title,Ref. No.,Copies
"~05151
~05152
~05153",CCEA GCSE English Language,425,4
"~C201151596
~C201151597",GCSE English Writing Skills,428,2
~09908,GCSE English Language and English for CCEA,428,1
~C201155080,CCEA GCSE English,425,1
~C201153189,Macbeth,822.3,1
~A0125917,The Shakespeare Library: Macbeth,822.3,1
~FFO1245690,Literature Guide for GCSE: Macbeth,822.3,1
~03736,Snap Revision Macbeth,822.3,1
~05162,CCEA GCSE History Fouth Edition,909.83,1
~FFO1245723,History for CCEA GCSE,909.82,1
~06296,CCEA GCSE Further Mathematics 2nd Edition,510,1
~018281,York Notes Of Mice and Men,825,1
~C20081851501,Revision Guide GCSE Intermediate/Higher,510,1
~C400447949,John Steinbeck's Of Mice and Men,813.52,1
"~05158
~05157
~05156",CCEA GCSE LLW 2nd Edition,302.14,3
"~C201034529
~C201034523
~C201034522
~C610432334D7",BBC Bitesize GCSE Religious Studies,230,4
"~C200992992
~C200992985",OCR GCSE Religious Studies World Religion(s) Christianity,230,2
~C201034971,Religion and Life Issues GCSE Religious Studies for AQA B Revision Guide,230,1
,CCEA GCSE Religious Studies An Introduction to Christian Ethics,,2"""

science_books_data = """Barcode,Title,Ref. No.,Copies
"~05148
~05149
~05150",CCEA GCSE Geography,910,3
"~05170
~05169",CCEA GCSE Chemistry,540,2
~05166,CCEA GCSE Biology,570,1
"~05159
~05161",CCEA GCSE Physics,530,2
"~05145
~05147",CCEA GCSE Digital Technology,4,2
"~C201155081
~05154
~C201155083
~05155",CCEA GCSE ICT,4,4"""

# YouTube links from edtech.html
youtube_links = {
    'physics': 'https://www.youtube.com/playlist?list=PLidqqIGKox7UVC-8WC9djoeBzwxPeXph7',
    'biology': 'https://www.youtube.com/playlist?list=PLidqqIGKox7X5UFT-expKIuR-i-BN3Q1g',
    'chemistry': 'https://www.youtube.com/playlist?list=PLidqqIGKox7WeOKVGHxcd69kKqtwrKl8W',
    'maths': 'https://www.youtube.com/playlist?list=PLidqqIGKox7XPh1QacLRiKto_UlnRIEVh'
}

def parse_books_data(data_string):
    """Parse CSV data and organize by subject"""
    books = {}
    lines = data_string.strip().split('\n')[1:]  # Skip header
    
    for line in lines:
        if not line.strip() or line.count(',') < 3:
            continue
            
        # Split by comma, but handle quoted fields
        parts = []
        current_part = ""
        in_quotes = False
        
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                parts.append(current_part.strip())
                current_part = ""
            else:
                current_part += char
        parts.append(current_part.strip())
        
        if len(parts) >= 4:
            barcode = parts[0].replace('"', '').replace('\n', ', ').strip()
            title = parts[1].strip()
            ref_no = parts[2].strip()
            copies = parts[3].strip()
            
            if title and copies:
                # Determine subject based on title keywords
                title_lower = title.lower()
                if 'english' in title_lower or 'macbeth' in title_lower or 'mice and men' in title_lower:
                    subject = 'english'
                elif 'history' in title_lower:
                    subject = 'history'
                elif 'mathematics' in title_lower or 'maths' in title_lower:
                    subject = 'maths'
                elif 'llw' in title_lower or 'life and work' in title_lower:
                    subject = 'learning-for-life-and-work'
                elif 'religious' in title_lower:
                    subject = 'religious-studies'
                elif 'geography' in title_lower:
                    subject = 'geography'
                elif 'chemistry' in title_lower:
                    subject = 'chemistry'
                elif 'biology' in title_lower:
                    subject = 'biology'
                elif 'physics' in title_lower:
                    subject = 'physics'
                elif 'digital technology' in title_lower:
                    subject = 'digital-technology'
                elif 'ict' in title_lower:
                    subject = 'digital-technology'  # ICT goes with Digital Technology
                else:
                    continue
                
                if subject not in books:
                    books[subject] = []
                
                books[subject].append({
                    'title': title,
                    'copies': copies,
                    'ref_no': ref_no
                })
    
    return books

def create_book_table_html(books_list, subject_name):
    """Create HTML table for books"""
    if not books_list:
        return f"""        <h3>Library books we have for {subject_name}</h3>
        <p>No books currently available for this subject.</p>"""
    
    html = f"""        <h3>Library books we have for {subject_name}</h3>
        <table class="book-table">
          <thead>
            <tr>
              <th>Title</th>
              <th>Copies</th>
            </tr>
          </thead>
          <tbody>"""
    
    for book in books_list:
        html += f"""
            <tr>
              <td>{book['title']}</td>
              <td>{book['copies']}</td>
            </tr>"""
    
    html += """
          </tbody>
        </table>"""
    
    return html

def add_youtube_button_html(youtube_url, subject_name):
    """Create YouTube button HTML"""
    return f"""                        <a class="placeholder-button youtube-button" href="{youtube_url}" target="_blank" title="YouTube Playlist">YouTube Playlist</a>"""

# Parse both book datasets
general_books = parse_books_data(general_books_data)
science_books = parse_books_data(science_books_data)

# Combine the datasets
all_books = general_books.copy()
for subject, books in science_books.items():
    if subject in all_books:
        all_books[subject].extend(books)
    else:
        all_books[subject] = books

print("Parsed books by subject:")
for subject, books in all_books.items():
    print(f"  {subject}: {len(books)} books")

# Update files with book tables and YouTube links
def update_file_with_books_and_youtube(filename, subject_mappings):
    """Update HTML file with book tables and YouTube links"""
    if not os.path.exists(filename):
        print(f"File {filename} does not exist")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for section_name, subject_key in subject_mappings.items():
        # Replace book list placeholder
        books_list = all_books.get(subject_key, [])
        book_table_html = create_book_table_html(books_list, section_name)
        
        # Pattern to find and replace the books placeholder
        book_pattern = f'(<h3>Library books we have for {re.escape(section_name)}</h3>\\s*<ul class="book-list"></ul>)'
        content = re.sub(book_pattern, book_table_html, content, flags=re.DOTALL)
        
        # Add YouTube button if available
        if subject_key in youtube_links:
            youtube_button = add_youtube_button_html(youtube_links[subject_key], section_name)
            
            # Find the placeholders div for this section and add YouTube button
            section_pattern = f'(<h2>{re.escape(section_name)}</h2>.*?<div class="placeholders">.*?)(</div>)'
            
            def add_youtube_to_section(match):
                before = match.group(1)
                after = match.group(2)
                # Check if YouTube button already exists
                if 'youtube-button' not in before:
                    return before + '\n' + youtube_button + '\n                      ' + after
                return match.group(0)
            
            content = re.sub(section_pattern, add_youtube_to_section, content, flags=re.DOTALL)
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename}")

# File mappings for updates
file_mappings = {
    'science.html': {
        'Biology': 'biology',
        'Chemistry': 'chemistry', 
        'Physics': 'physics'
    },
    'english.html': {
        'English Language': 'english',
        'English Literature': 'english'
    },
    'maths.html': {
        'GCSE Maths': 'maths',
        'Further Mathematics': 'maths'
    },
    'history.html': {
        'History': 'history'
    },
    'religious-studies.html': {
        'Religious Studies': 'religious-studies'
    },
    'geography.html': {
        'Geography': 'geography'
    },
    'digital-technology.html': {
        'Digital Technology': 'digital-technology'
    },
    'learning-for-life-and-work.html': {
        'Learning for Life and Work': 'learning-for-life-and-work'
    }
}

# Update all files
for filename, mappings in file_mappings.items():
    update_file_with_books_and_youtube(filename, mappings)

print("Book tables and YouTube links update completed!")