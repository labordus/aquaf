; -- aquaf.iss --
; Versie 0.84-alpha 

[Setup]
AppName=Aquaf
AppVersion=0.84-alpha
;AppVerName=version 0.84-alpha
DefaultDirName={pf}\Aquaf
DefaultGroupName=Aquaf
Compression=lzma
SolidCompression=yes
AppReadmeFile=README.md
VersionInfoVersion=0.84
OutputBaseFilename=aquaf

[Files]
Source: "aquaf.exe"; DestDir: "{app}"
Source: "aquaf.db"; DestDir: "{localappdata}\aquaf"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "README.md"; DestDir: "{app}"; Flags: isreadme
Source: "MSVCR90.dll"; DestDir: "{app}"
Source: "forumbanner.gif"; DestDir: "{app}"
Source: "icon.ico"; DestDir: "{app}"
Source: "favicon.ico"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "dagterug.bmp"; DestDir: "{app}"
Source: "dagverder.bmp"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "archive.html"; DestDir: "{app}"; Flags: uninsneveruninstall
Source: "image.css"; DestDir: "{app}"; Flags: uninsneveruninstall
Source: "aquaf.json"; DestDir: "{app}"; Flags: onlyifdoesntexist uninsneveruninstall

[Icons]
Name: "{group}\Aquaf v0.84-alpha"; Filename: "{app}\aquaf.exe"
Name: "{group}\Uninstall Aquaf"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\aquaf.exe"; Description: "Start het programma"; Flags: postinstall nowait skipifsilent unchecked

[UninstallDelete]
Type: files; Name: "{app}\tempfile.dat"
Type: files; Name: "{app}\aquaf.exe.log"

[LangOptions]
LanguageID=$0413

[Languages]
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"
