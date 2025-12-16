import re
import glob

# Get all HTML files
html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count matches before
    before_count = len(re.findall(r'src="\.\.\/', content))
    
    # Replace ../ with nothing in src attributes
    new_content = re.sub(r'src="\.\.\/', 'src="', content)
    new_content = re.sub(r'src="\.\./\.\.\/', 'src="', new_content)
    
    # Count matches after
    after_count = len(re.findall(r'src="\.\.\/', new_content))
    
    if before_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'{filepath}: Fixed {before_count} paths')
    
print('Done!')
