; -- aquaf.iss --
; Versie 0.85

[Setup]
AppName=Aquaf
AppVersion=0.85
;AppVerName=version 0.85
DefaultDirName={pf}\Aquaf
DefaultGroupName=Aquaf
Compression=lzma
SolidCompression=yes
VersionInfoVersion=0.85
OutputBaseFilename=aquaf085_setup
AppPublisher=kellemes

[Files]
Source: "aquaf.exe"; DestDir: "{app}"
Source: "README.md"; DestDir: "{app}"
Source: "MSVCR90.dll"; DestDir: "{app}"
Source: "forumbanner.gif"; DestDir: "{app}"
Source: "icon.ico"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "front.jpg"; DestDir: "{app}"
Source: "archive.html"; DestDir: "{localappdata}\aquaf"
Source: "fotorama.js"; DestDir: "{localappdata}\aquaf"
Source: "favicon.ico"; DestDir: "{localappdata}\aquaf"

[Icons]
Name: "{group}\Aquaf"; Filename: "{app}\aquaf.exe"
Name: "{group}\Uninstall Aquaf"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\aquaf.exe"; Flags: postinstall nowait skipifsilent; Description: "Start het programma"

[UninstallDelete]
Type: files; Name: "{app}\aquaf.exe.log"

[LangOptions]
LanguageID=$0413

[Languages]
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"

[InstallDelete]
Type: files; Name: "{group}\Aquaf v0.84.lnk"
