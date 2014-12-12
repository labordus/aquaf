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
VersionInfoVersion=0.84
OutputBaseFilename=aquaf
AppPublisher=kellemes

[Files]
Source: "aquaf.exe"; DestDir: "{app}"
Source: "README.md"; DestDir: "{app}"
Source: "MSVCR90.dll"; DestDir: "{app}"
Source: "forumbanner.gif"; DestDir: "{app}"
Source: "icon.ico"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "archive.html"; DestDir: "{localappdata}\aquaf"
Source: "favicon.ico"; DestDir: "{localappdata}\aquaf"

[Icons]
Name: "{group}\Aquaf v0.84-alpha"; Filename: "{app}\aquaf.exe"
Name: "{group}\Uninstall Aquaf"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\aquaf.exe"; Description: "Start het programma"; Flags: postinstall nowait skipifsilent unchecked

[UninstallDelete]
Type: files; Name: "{app}\aquaf.exe.log"

[LangOptions]
LanguageID=$0413

[Languages]
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"
