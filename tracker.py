#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade
import urllib
import json

########################
# Travis API addresses #
########################

repos = 'http://travis-ci.org/repositories.json'
reposByOwner = 'http://travis-ci.org/repositories.json?owner_name=:owner'
reposIndexSearch = 'http://travis-ci.org/repositories.json?search=:query'
reposShow = 'http://travis-ci.org/:owner_name/:name.json'
builds = 'http://travis-ci.org/:owner_name/:name/builds.json'
buildsShow = 'http://travis-ci.org/:owner_name/:name/builds/:id.json'
workers = 'http://travis-ci.org/workers.json'
jobs = 'http://travis-ci.org/jobs.json'
jobsShow = 'http://travis-ci.org/jobs/:id.json'


class TravisCIUsername:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/mainWindow.glade")

        self.mainWindow = self.builder.get_object("window1")
        self.okButton = self.builder.get_object("okButton")
        self.travisName = self.builder.get_object("entryUser")
        self.builder.connect_signals(self)

    def on_okButton_clicked(self, widget):
        builds = json.loads(urllib.urlopen(reposByOwner.replace(':owner', self.travisName.get_text())).read())
        if not builds:
            error = ErrorUserName()
            error.dialog.show()
        else:
            s = ShoWBuilds()
            s.window.show()

    def gtk_main_quit(self, widget):
        gtk.main_quit()


class ErrorUserName:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/noUser.glade")

        self.dialog = self.builder.get_object("messagedialog1")
        self.backButton = self.builder.get_object("backButton")
        self.builder.connect_signals(self)

    def on_backButton_clicked(self, widget):
        self.dialog.destroy()


class ShoWBuilds:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/showBuilds.glade")

        self.window = self.builder.get_object("window1")
        self.listOfBuilds = self.builder.get_object("buildsList")
        self.listOfBuilds.append(('blabla',''))


    def gtk_main_quit(self, widget):
        gtk.main_quit()

if __name__ == "__main__":
    a = TravisCIUsername()
    a.mainWindow.show()
    gtk.main()