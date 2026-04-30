#!/usr/bin/env python3
import os

# CSS styles for book tables and YouTube buttons
table_css = """
/* Book table styles */
.book-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 12px;
  background: rgba(255,255,255,0.95);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.book-table th {
  background: #0f3044;
  color: white;
  padding: 12px;
  text-align: left;
  font-weight: 600;
}

.book-table td {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(0,0,0,0.08);
}

.book-table tr:nth-child(even) {
  background: rgba(240,248,255,0.5);
}

.book-table tr:hover {
  background: rgba(226,245,255,0.7);
}

/* YouTube button styles */
.youtube-button {
  background: #ff4444 !important;
  border-color: #cc3333 !important;
  color: white !important;
}

.youtube-button:hover {
  background: #ee3333 !important;
}
"""

# List of CSS files to update
css_files = [
    'css/science.css',
    'css/english.css', 
    'css/maths.css',
    'css/history.css',
    'css/religious-studies.css',
    'css/geography.css',
    'css/digital-technology.css',
    'css/learning-for-life-and-work.css',
    'css/business-studies.css',
    'css/design-technology.css',
    'css/languages.css',
    'css/media-studies.css',
    'css/motor-vehicle-studies.css',
    'css/physical-education.css'
]

def add_styles_to_css_file(filename):
    """Add table and YouTube button styles to CSS file"""
    if not os.path.exists(filename):
        print(f"File {filename} does not exist")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if styles already exist
    if '.book-table' in content:
        print(f"Styles already exist in {filename}")
        return
    
    # Add the new styles at the end
    updated_content = content + table_css
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Added table styles to {filename}")

# Update all CSS files
for css_file in css_files:
    add_styles_to_css_file(css_file)

print("CSS styles update completed!")