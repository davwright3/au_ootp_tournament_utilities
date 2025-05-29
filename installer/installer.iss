[Setup]
AppName=AU Tournament Utilities
AppVersion=0.1.1
DefaultDirName={autopf}\AU_Tournament_Utilities
DefaultGroupName=AU Tournament Utilities
OutputDir=Output
OutputBaseFilename=AU_Tournament_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "{#MyOutputDir}*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\AU Tournament Utilities"; Filename: "{app}\main.exe"
Name: "{commondesktop}\AU Tournament Utilities"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"