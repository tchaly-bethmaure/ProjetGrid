#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# variables utilisées
name_of_file = "tail5authlog"
default_path = "/root/scpy"
storage_remote_name = "supervisor"

print("Installing 7zip if needed.")
os.system("apt-get install -yq p7zip")

print("Zipping this file.")
os.system("7z a "+ default_path +"/logfile.7z "+ default_path +"/"+ name_of_file)

print("Removing original file : " + name_of_file)
os.system("rm "+default_path+"/"+name_of_file)

# marche, mais à tenter si la config du réseau est stable
#print("Fetch it on remote storage : "+storage_remote_name+".")
#os.system("clush -w "+ storage_remote_name +" --copy "+ default_path)

print("Done.")
