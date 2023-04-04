import os

# Create a new directory for the transformed images
transformed_dir = 'transformed_images'
if not os.path.exists(transformed_dir):
    os.makedirs(transformed_dir)

# Asking the user for the desired transformation
print('Enter the number corresponding to the desired transformation:')
print('1. Automatic (using EXIF orientation tag)')
print('2. Flip vertically')
print('3. Flip horizontally')
print('4. Rotate 90 degrees clockwise')
print('5. Rotate 180 degrees clockwise')
print('6. Rotate 270 degrees clockwise')

choice = int(input())

# Choose the appropriate exiftran command based on the user's choice
if choice == 1:
    command = 'exiftran -a'
elif choice == 2:
    command = 'exiftran -f'
elif choice == 3:
    command = 'exiftran -F'
elif choice == 4:
    command = 'exiftran -9'
elif choice == 5:
    command = 'exiftran -1'
elif choice == 6:
    command = 'exiftran -2'

# Transform all jpeg and jpg files in the current directory
for filename in os.listdir():
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        os.system(f'{command} "{filename}" -o "{transformed_dir}/{filename}"')

print('Done!')

