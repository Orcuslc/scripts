import os, sys
import subprocess

#source=r"/run/media/chuan/Seagate Backup Plus Drive/CD/企鹅三星带花100专辑 233CD"
#target=r"/run/media/chuan/Seagate Backup Plus Drive/CD/Penguin Guide Rosette"

source=r'/run/media/chuan/Seagate Backup Plus Drive/CD/DG大禾花系列 244CD'
target=r'/run/media/chuan/Seagate Backup Plus Drive/CD/DG The Originals'

for folder in os.listdir(source):
    src = os.path.join(source, folder)
    dst = os.path.join(target, folder)
    try:
        os.mkdir(dst)
    except FileExistsError:
        pass

    for f in os.listdir(src):
        print(f)
        if f == "CDImage.ape":
            subprocess.call(["cp", os.path.join(src, f), os.path.join(dst, "CDImage.ape")])
        elif os.path.isdir(os.path.join(src, f)) and f[0] == 'C':
            sub_src = os.path.join(src, f)
            print(os.path.join(sub_src, "CDImage.ape"))
            print(os.path.join(dst, "{0}.ape".format(f)))
            subprocess.call(["cp", os.path.join(sub_src, "CDImage.ape"), os.path.join(dst, "{0}.ape".format(f))])
        elif os.path.isfile(os.path.join(src, f)) and (f.endswith('jpg') or f.endswith('JPG')):
            subprocess.call(["cp", os.path.join(src, f), os.path.join(dst, f)])
