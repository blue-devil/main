#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools

WorkDir = "."

def setup():
	cmaketools.configure("-DCMAKE_BUILD_TYPE=Release -B_build -G Ninja -L")

def build():
	mesontools.build("-C _build")

def install():
	mesontools.install("-C _build")
