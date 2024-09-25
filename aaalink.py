import os
import re

def convert_wikilinks_to_markdown(directory):
    # Define the regex pattern to find links like ![[Pasted image 20240920111444.png]]
    wikilink_pattern = r'!\[\[(.*?)\]\]'
    
    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find all instances of the image links
                matches = re.findall(wikilink_pattern, content)
                
                # If there are matches, replace them with Markdown-style image links
                if matches:
                    print(f"Processing {file_path}...")

                    # Replace each occurrence with the markdown image format
                    def replace_wikilink(match):
                        image_file = match.group(1).strip()  # Extract the image file name
                        return f"![{image_file}](Images/{image_file})"
                    
                    # Substituting all found patterns with the Markdown style image links
                    new_content = re.sub(wikilink_pattern, replace_wikilink, content)
                    
                    # Write the updated content back to the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    print(f"Converted image links in {file_path}.")

if __name__ == "__main__":
    directory = "obsidian"
    convert_wikilinks_to_markdown(directory)
