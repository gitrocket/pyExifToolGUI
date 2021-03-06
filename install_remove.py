#!/usr/bin/env python

# install_remove.py

# Copyright (c) 2012-2013 Harry van der Wolf. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public Licence as published
# by the Free Software Foundation, either version 2 of the Licence, or
# version 3 of the Licence, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public Licence for more details.

# This file is part of pyexiftoolgui.
# pyexiftoolgui is a pySide script program that reads and writes  
# gps tags from/to files. It can use a "reference" image to write the
# gps tags to a multiple set of files that are taken at the same
# location.
# pyexiftoolgui is a graphical frontend for the open source
# command line tool exiftool by Phil Harvey, but it's not
# a complete exiftool gui: not at all.

import os, sys, platform


def print_usage():
    print "\nUsage of this script:"
    print "sudo ./install_remove.py install     : This will install pyExifToolGui on your system"
    print "sudo ./install_remove.py remove      : This will remove pyExifToolGui from your system\n\n"
    sys.exit()

def darwin_install():
    os.system('rm -f scripts/*.pyc scripts/*~ ui/*.pyc ui/*~')
    copyapp = os.system('cp -a MacOSX/pyExifToolGUI.app /Applications')
    copyrest = os.system('cp -a COPYING scripts manual /Applications/pyExifToolGUI.app/Contents/Resources/')
    print "\nYou will find a pyExifToolGui.app in your Applications folder."
    print "This app only contains the scripts for the application itself."
    print "Make sure that you install QT4 and pyside on your system.\n"
    sys.exit()

def windows_install():
    print("\nSorry. There is no installation script available for windows")
    print("You can download the full application in a zip file from where")
    print("you got this version as well.")
    sys.exit()

#------------------------------------------------------------------------
# main
OSplatform = platform.system()
if OSplatform != "Windows":
   if os.geteuid() != 0:
      print '\n#### Script must be run with root authorization. ####'
      print_usage()
   


if len(sys.argv) == 1:
   print_usage()
elif len(sys.argv) == 2:
   prefix_path = os.path.join('/', 'usr', 'local')
   usr_bin_path = os.path.join(prefix_path, 'bin')
   usr_share_path = os.path.join(prefix_path, 'share')
   pyexiftoolgui_path = os.path.join(usr_share_path, 'pyexiftoolgui')
   if "install" in sys.argv:
      OSplatform = platform.system()
      if OSplatform == "Darwin":
           darwin_install()
      if OSplatform == "Windows":
           windows_install()
      print "\nYou have chosen to install pyExiftoolGUI on your system"
      print "\n=======================================================\n"
      os.system("python setup.py install --install-layout=deb --install-lib=" + pyexiftoolgui_path + " --install-scripts=" + usr_bin_path)
      print "\n======================================================="
      print "\nIf you didn't see errors on your screen, pyExifToolGui has been installed."
      print "In case of errors contact me."
      print "You might also see a lot of \"kbuildsycoca4\" messages."
      print "This is the cache being rebuilt and your application"
      print "being added to menus and so on.\n"

   # remove pyexiftoolgui
   elif "remove" in sys.argv:
      try:
            #fldr = shutil.rmtree(pyexiftoolgui_path)
            fldr = os.system('rm -rf ' + pyexiftoolgui_path)
      except:
            print "Could not remove " + pyexiftoolgui_path
      try:
            #result = os.remove('/usr/bin/pyexiftoolgui')
            result = os.system('rm -rf ' + os.path.join(usr_bin_path, 'pyexiftoolgui'))
      except:
            print "Could not remove " + os.path.join(usr_bin_path, 'pyexiftoolgui')
      try:
            #result = os.remove(os.path.join(usr_share_path, 'applications', 'pyexiftoolgui.desktop'))
            result = os.system('rm -rf ' + os.path.join(usr_share_path, 'applications', 'pyexiftoolgui.desktop'))
      except:
            print "Could not remove " + os.path.join(usr_share_path, 'applications', 'pyexiftoolgui.desktop')
      try:
            #result = os.remove(os.path.join(usr_share_path, 'pixmaps', 'pyexiftoolgui.png'))
            result = os.system('rm -rf ' + os.path.join(usr_share_path, 'pixmaps', 'pyexiftoolgui.png'))
      except:
            print "Could not remove " + os.path.join(usr_share_path, 'pixmaps', 'pyexiftoolgui.png')
   # Some non-existent option or --help or --hlp for example
   else:
      print_usage()
else: # More than 2 arguments
   print_usage()

