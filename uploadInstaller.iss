; -- aquaf.iss --
; Versie 0.84 

[Setup]
AppName=Aquaf
AppVerName=version 0.84
DefaultDirName={pf}\Aquaf
DefaultGroupName=Aquaf
Compression=lzma
SolidCompression=yes

[Files]
Source: "main.exe"; DestDir: "{app}"
Source: "README.md"; DestDir: "{app}"
Source: "MSVCR90.dll"; DestDir: "{app}"
Source: "forumbanner.gif"; DestDir: "{app}"
Source: "icon.ico"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "dagterug.bmp"; DestDir: "{app}"
Source: "dagverder.bmp"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "archive.html"; DestDir: "{app}"; Flags: uninsneveruninstall
Source: "image.css"; DestDir: "{app}"; Flags: uninsneveruninstall
Source: "images.json"; DestDir: "{app}"; Flags: onlyifdoesntexist uninsneveruninstall

[Icons]
Name: "{group}\Aquaf v0.84"; Filename: "{app}\main.exe"
Name: "{group}\Uninstall Aquaf"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\main.exe"; Description: "Start het programma"; Flags: postinstall nowait skipifsilent unchecked

[UninstallDelete]
Type: files; Name: "{app}\tempfile.dat"
Type: files; Name: "{app}\main.exe.log"