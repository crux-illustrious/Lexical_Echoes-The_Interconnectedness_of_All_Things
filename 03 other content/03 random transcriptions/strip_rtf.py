from striprtf.striprtf import rtf_to_text

# Define the path to your RTF file (update the path as needed)
rtf_file_path = "instagram threats transcribed.rtf"

# Read the RTF file
with open(rtf_file_path, 'r', encoding='utf-8') as file:
    rtf_content = file.read()

# Convert RTF content to plain text
plain_text = rtf_to_text(rtf_content)

# Save the plain text to a new file
output_file_path = "instagram_threats_plain.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(plain_text)

print(f"Plain text has been saved to {output_file_path}")