import os
import shutil
from tqdm import tqdm
from pathlib import Path
import time

Text = [".doc",".docx",",.log",".odt",".txt",".rtf",".msg",".pages",".tex",".wpd",".wps"]
Data = [".pdf",".xls","xlsx",".cvs",".ini",".dat",".ged",".key",".keychain",".pps",".ppt",".pptx",".sdf",".xlr"]
Audio = [".aif",".iff",".m3u",".m4a",".mid",".mp3",".mpa",".wav",".wma",".ogg",".aac"]
Video = [".3g2",".3gp",".asf",".avi",".flv",".m4v",".mov",".mp4",".mpg",".rm",".srt",".swf",".vob","wmv",".mkv"]
Image = [".3dm",".3ds",".max",".obj",".bmp",".dds",".gif",".heic",".jpg",".jpeg",".png",".psd",".pspimage",".tga",".thm",".tif",".tiff",".yuv",".ai",".eps",".ps",".svg"]
Database = [".accdb",".db",".dbf",".mdb",".pdb",".sql"]
Executable = [".apk",".app",".bat",".cgi",".com",".exe",".gadget",".jar",".wsf"]
Game = [".b",".dem",".gam",".nes",".rom",".sav"]
Cad = [".dwg",".dxf"]
Gis = [".gpx",".kml",".kmz"]
Web = [".asp",".aspx",".cer",".cfm",".csr",".css",".dcr",".htm",".html",".js",".jsp",".php",".rss",".xhtml"]
Plugin = [".crx",".plugin"]
Font = [".fnt",".fon",".otf",".ttf"]
System = [".cab",".cpl",".cur",".deskthemepack",".dll",".dmp",".drv",".icns",".ico",".lnk",".sys"]
Settings = [".cfg",".config",".ini",".prf"]
Compressed = [".7z",".cbr",".deb",".gz",".pkg",".rar",".rpm",".sitx",".tar",".tar.gz",".zip",".zipx"]
DiskImage = [".iso",".cue",".dmg",".iso",".mdf",".toast",".vcd"]
Developer = [".c",".class",".cpp",".cs",".dtd",".fla",".h",".java",".lua",".m",".pl",".py",".sh",".go",".sln",".swift",".vb",".vcxproj",".xcodeproj"]
BackUp = [".bak",".tmp"]
Misc = [".crdownload",".ics",".msi",".part",".torrent"]

dizin = input("Hangi dizinden başlatmak istersiniz.")

os.chdir(dizin)
print(os.getcwd())
print("\033[0;37;40m\nKlasörleme İşlemi yapılıyor...\033[1;m")

for i in tqdm(range(0,32)): 

    for i in os.listdir(os.getcwd()):
        a,b = os.path.splitext(i)
        if b in Text:
            if os.path.exists("Text"):
                shutil.move(dizin+'/'+i , dizin+'/Text/'+i)
            else:
                os.mkdir("Text")
                shutil.move(dizin+'/'+i , dizin+'/Text/'+i)

        if b in Data:
            if os.path.exists("Data"):
                shutil.move(dizin+'/'+i , dizin+'/Data/'+i)
            else:
                os.mkdir("Data")
                shutil.move(dizin+'/'+i , dizin+'/Data/'+i)

        if b in Audio:
            if os.path.exists("Audio"):
                shutil.move(dizin+'/'+i , dizin+'/Audio/'+i)
            else:
                os.mkdir("Audio")
                shutil.move(dizin+'/'+i , dizin+'/Audio/'+i)

        if b in Video:
            if os.path.exists("Video"):
                shutil.move(dizin+'/'+i , dizin+'/Video/'+i)
            else:
                os.mkdir("Video")
                shutil.move(dizin+'/'+i , dizin+'/Video/'+i)

        if b in Image:
            if os.path.exists("Image"):
                shutil.move(dizin+'/'+i , dizin+'/Image/'+i)
            else:
                os.mkdir("Image")
                shutil.move(dizin+'/'+i , dizin+'/Image/'+i)

        if b in Database:
            if os.path.exists("Database"):
                shutil.move(dizin+'/'+i , dizin+'/Database/'+i)
            else:
                os.mkdir("Database")
                shutil.move(dizin+'/'+i , dizin+'/Database/'+i)
    
        if b in Executable:
            if os.path.exists("Executable"):
                shutil.move(dizin+'/'+i , dizin+'/Executable/'+i)
            else:
                os.mkdir("Executable")
                shutil.move(dizin+'/'+i , dizin+'/Executable/'+i)
            
        if b in Game:
            if os.path.exists("Game"):
                shutil.move(dizin+'/'+i , dizin+'/Game/'+i)
            else:
                os.mkdir("Game")
                shutil.move(dizin+'/'+i , dizin+'/Game/'+i)

        if b in Cad:
            if os.path.exists("Cad"):
                shutil.move(dizin+'/'+i , dizin+'/Cad/'+i)
            else:
                os.mkdir("Cad")
                shutil.move(dizin+'/'+i , dizin+'/Cad/'+i)

        if b in Gis:
            if os.path.exists("Gis"):
                shutil.move(dizin+'/'+i , dizin+'/Gis/'+i)
            else:
                os.mkdir("Gis")
                shutil.move(dizin+'/'+i , dizin+'/Gis/'+i)

        if b in Web:
            if os.path.exists("Web"):
                shutil.move(dizin+'/'+i , dizin+'/Web/'+i)
            else:
                os.mkdir("Web")
                shutil.move(dizin+'/'+i , dizin+'/Web/'+i)

        if b in Plugin:
            if os.path.exists("Plugin"):
                shutil.move(dizin+'/'+i , dizin+'/Plugin/'+i)
            else:
                os.mkdir("Plugin")
                shutil.move(dizin+'/'+i , dizin+'/Plugin/'+i)

        if b in Font:
            if os.path.exists("Font"):
                shutil.move(dizin+'/'+i , dizin+'/Font/'+i)
            else:
                os.mkdir("Font")
                shutil.move(dizin+'/'+i , dizin+'/Font/'+i)

        if b in System:
            if os.path.exists("System"):
                shutil.move(dizin+'/'+i , dizin+'/System/'+i)
            else:
                os.mkdir("System")
                shutil.move(dizin+'/'+i , dizin+'/System/'+i)

        if b in Settings:
            if os.path.exists("Settings"):
                shutil.move(dizin+'/'+i , dizin+'/Settings/'+i)
            else:
                os.mkdir("Settings")
                shutil.move(dizin+'/'+i , dizin+'/Settings/'+i)

        if b in Compressed:
            if os.path.exists("Compressed"):
                shutil.move(dizin+'/'+i , dizin+'/Compressed/'+i)
            else:
                os.mkdir("Compressed")
                shutil.move(dizin+'/'+i , dizin+'/Compressed/'+i)

        if b in DiskImage:
            if os.path.exists("DiskImage"):
                shutil.move(dizin+'/'+i , dizin+'/DiskImage/'+i)
            else:
                os.mkdir("DiskImage")
                shutil.move(dizin+'/'+i , dizin+'/DiskImage/'+i)

        if b in Developer:
            if os.path.exists("Developer"):
                shutil.move(dizin+'/'+i , dizin+'/Developer/'+i)
            else:
                os.mkdir("Developer")
                shutil.move(dizin+'/'+i , dizin+'/Developer/'+i)

        if b in BackUp:
            if os.path.exists("BackUp"):
                shutil.move(dizin+'/'+i , dizin+'/BackUp/'+i)
            else:
                os.mkdir("BackUp")
                shutil.move(dizin+'/'+i , dizin+'/BackUp/'+i)

        if b in Misc:
            if os.path.exists("Misc"):
                shutil.move(dizin+'/'+i , dizin+'/Misc/'+i)
            else:
                os.mkdir("Misc")
                shutil.move(dizin+'/'+i , dizin+'/Misc/'+i)

        time.sleep(0.02)

print("\033[0;37;40m\nKlasörleme İşlemi Bitti...\033[1;m")
