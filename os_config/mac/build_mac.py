import os
import sys
import shutil
import subprocess
from dotenv import load_dotenv

load_dotenv()


def resource_path(relative_path):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir, relative_path))


appName = os.getenv('APP_NAME')  # money-manager-python
base_path = os.path.dirname(os.path.abspath(__file__))

# Get the root directory
root_directory = os.path.dirname(os.path.dirname(base_path))

generatedDir = os.path.join(base_path, '_generated')
# resourceDir = resource_path(os.path.join(root_directory, 'src', 'resources'))
# systemTrayResDir = resource_path(os.path.join(resourceDir, 'images', 'system_tray'))

print('---------------------------------------------')
print('---------------------------------------------')
print('---------------------------------------------')
print(f'APP_NAME: {appName}')
print(f'root_directory:   {root_directory}')
print(f'base_path:        {base_path}')
print(f'generatedDir:     {generatedDir}')
# print(f'resourceDir:      {resourceDir}')
# print(f'systemTrayResDir: {systemTrayResDir}')
print('---------------------------------------------')
print('---------------------------------------------')
print('---------------------------------------------\n')

# Clear: delete generatedDir directory
if os.path.exists(generatedDir):
    print('\nClearing generatedDir directory...')
    shutil.rmtree(generatedDir)
    print('Cleared generatedDir directory.\n')

# Step 0: give some info
subprocess.run([
    'echo',
    # f'{print(os.environ)}'
    f'\nBuilding {appName}.app for Mac... (this may take a while; destination: {generatedDir})\n',
])

# Step 1: Create the executable
subprocess.run([
    'pyinstaller',
    '--onefile',
    "--windowed",
    f"--distpath={generatedDir}/dist",
    f"--workpath={generatedDir}/build",
    f"--specpath={generatedDir}",
    f"--add-data={root_directory}/images/test.png:images",
    f"--name={appName}",
    f"{root_directory}/main.py"
])

# # Step 2: Create the .app bundle
# subprocess.run(['mkdir', f'{appName}.app'])
# subprocess.run(['mkdir', '-p', f'{appName}.app/Contents/MacOS'])
# subprocess.run(['mv', f'dist/{appName}', f'{appName}.app/Contents/MacOS/'])
#
# # Optionally, create an Info.plist file here
# subprocess.run([
#     "/usr/libexec/PlistBuddy",
#     "-c",
#     "Add :CFBundleURLTypes array",
#     f"dist/{appName}.app/Contents/Info.plist",
# ])
# subprocess.run([
#     "/usr/libexec/PlistBuddy",
#     "-c",
#     "Add :CFBundleURLTypes:0 dict",
#     f"dist/{appName}.app/Contents/Info.plist",
# ])
# subprocess.run([
#     "/usr/libexec/PlistBuddy",
#     "-c",
#     "Add :CFBundleURLTypes:0:CFBundleURLSchemes array",
#     f"dist/{appName}.app/Contents/Info.plist",
# ])
# subprocess.run([
#     "/usr/libexec/PlistBuddy",
#     "-c",
#     f"Add :CFBundleURLTypes:0:CFBundleURLSchemes:0 string {appName}",
#     f"dist/{appName}.app/Contents/Info.plist",
# ])
#
# # Step 3: Create the DMG file
# subprocess.run([
#     '/path_to/create-dmg/create-dmg',
#     '--volname', f'{appName}',
#     '--volicon', f'os_config/mac/images/installer/installer-icon.png',
#     '--background', 'os_config/mac/images/installer/background-installer.png',
#     '--window-pos', '200', '120',
#     '--window-size', '800', '400',
#     '--icon-size', '100',
#     '--icon', f'{appName}.app', '200', '190',
#     '--hide-extension', f'{appName}.app',
#     '--app-drop-link', '600', '185',
#     f'{appName}.dmg',
#     f'{appName}.app',
# ])
