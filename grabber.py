# python C:\wamp64\www\apps\ftpThumbGrabber\grabber.py
from pathlib import Path
from ftplib import FTP
import datetime
import loginDetails

print(loginDetails.username)


local = "D:/camFootage/snaps/"
camDetails = ["192.168.0.109","/IPCamera/C2_00626E830E4B/snap/"]
camDetails = ["192.168.0.107","/IPCamera/C2_00626E830EB6/snap/"]
getDirDate = "20190516"
  
def run():
    camIp = camDetails[0]
    camDir = camDetails[1]
    username = loginDetails.username
    password = loginDetails.password

    ftp = FTP()
    ftp.connect(camIp,50021)
    ftp.login(username, password)
    ftp.cwd(camDir)
    dirs = []
    ftp.dir(dirs.append)
    found = False
    for d in dirs:
        if d.rfind(getDirDate) > -1:
            found = True

    if found==False:
        print('not found'+getDirDate)
        return False

    ftp.cwd(camDir+getDirDate)
    subdirs = []
    ftp.dir(subdirs.append)
    subdirs = [x.split(' ')[-1] for x in subdirs]
    #print(subdirs)
    #subdirs = subdirs[0].split(' ')[-1]
    for subdir in subdirs:
        print(subdir.split(' ')[-1])
        ftp.cwd(camDir+getDirDate+"/"+subdir+"/")
        snaps = []
        ftp.dir(snaps.append)
        snaps = [x.split(' ')[-1] for x in snaps]
        print(snaps)
        for snap in snaps:
            localSubdir = Path(local+getDirDate)
            if localSubdir.is_dir()==False:
                localSubdir.mkdir()
            localSnap = Path(local+getDirDate+"/"+snap)
            if localSnap.is_file()==False:
                print("downloading file:"+snap)
                with open(local+getDirDate+"/"+snap, 'wb') as f:
                    ftp.retrbinary('RETR ' + snap, f.write)                        
            #break
        #break

    print('finished script')


#run()

