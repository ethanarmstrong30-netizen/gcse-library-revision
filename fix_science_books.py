#!/usr/bin/env python3
import re
import os

# Correct science books data from the CSV
science_books_data = {
    'geography': [{'title': 'CCEA GCSE Geography', 'copies': '3'}],
    'chemistry': [{'title': 'CCEA GCSE Chemistry', 'copies': '2'}],
    'biology': [{'title': 'CCEA GCSE Biology', 'copies': '1'}],
    'physics': [{'title': 'CCEA GCSE Physics', 'copies': '2'}],
    'digital-technology': [
        {'title': 'CCEA GCSE Digital Technology', 'copies': '2'},
        {'title': 'CCEA GCSE ICT', 'copies': '4'}
    ]
}

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

def update_science_books():
    """Update science.html with correct book data"""
    filename = 'science.html'
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Chemistry section
    chemistry_books = science_books_data.get('chemistry', [])
    chemistry_table = create_book_table_html(chemistry_books, 'Chemistry')
    content = re.sub(
        r'(<h3>Library books we have for Chemistry</h3>\s*<p>No books currently available for this subject\.</p>)',
        chemistry_table,
        content,
        flags=re.DOTALL
    )
    
    # Update Physics section
    physics_books = science_books_data.get('physics', [])
    physics_table = create_book_table_html(physics_books, 'Physics')
    content = re.sub(
        r'(<h3>Library books we have for Physics</h3>\s*<p>No books currently available for this subject\.</p>)',
        physics_table,
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated science.html with correct book data")

def update_other_science_subjects():
    """Update other science subject files"""
    
    # Update geography.html
    geography_books = science_books_data.get('geography', [])
    geography_table = create_book_table_html(geography_books, 'Geography')
    
    with open('geography.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'(<h3>Library books we have for Geography</h3>\s*<ul class="book-list"></ul>)',
        geography_table,
        content,
        flags=re.DOTALL
    )
    
    with open('geography.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated geography.html")
    
    # Update digital-technology.html
    digital_books = science_books_data.get('digital-technology', [])
    digital_table = create_book_table_html(digital_books, 'Digital Technology')
    
    with open('digital-technology.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'(<h3>Library books we have for Digital Technology</h3>\s*<ul class="book-list"></ul>)',
        digital_table,
        content,
        flags=re.DOTALL
    )
    
    with open('digital-technology.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated digital-technology.html")

# Run the updates
update_science_books()
update_other_science_subjects()

print("Science books update completed!")