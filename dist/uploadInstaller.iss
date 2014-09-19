; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=Aquaforum Uploader
AppVerName=version 0.83
DefaultDirName={pf}\AquaforumUploader
DefaultGroupName=Aquaforum
Compression=lzma
SolidCompression=yes

[Files]
Source: "aquaforumUpload.exe"; DestDir: "{app}"
Source: "MSVCR71.dll"; DestDir: "{app}"
Source: "w9xpopen.exe"; DestDir: "{app}"
Source: "forumbanner.gif"; DestDir: "{app}"
Source: "icon.ico"; DestDir: "{app}"
Source: "test.jpg"; DestDir: "{app}"
Source: "archive.html"; DestDir: "{app}"; Flags: uninsneveruninstall
Source: "images.json"; DestDir: "{app}"; Flags: onlyifdoesntexist uninsneveruninstall

[Icons]
Name: "{group}\Aquaforum v0.82"; Filename: "{app}\aquaforumUpload.exe"
Name: "{group}\Uninstall AquaforumUploader"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\aquaforumUpload.exe"; Description: "Start het programma"; Flags: postinstall nowait skipifsilent unchecked

[UninstallDelete]
Type: files; Name: "{app}\tempfile.dat"
Type: files; Name: "{app}\aquaforumUpload.exe.log"
