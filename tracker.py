#!/usr/bin/env python

import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade
import travisParser


class TravisCIUsername:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/mainWindow.glade")
        self.builder.connect_signals(self)

        self.mainWindow = self.builder.get_object("window1")
        self.okButton = self.builder.get_object("okButton")
        self.travisName = self.builder.get_object("entryUser")

    def on_okButton_clicked(self, widget):
        builds, jobs = travisParser.getBuildsAndJobs(self.travisName.get_text())
        if not builds:
            error = ShowDialog("Error!", "This username doesn't appear to be valid.")
            error.dialog.show()
        else:
            s = ShoWBuildsAndJobs(builds, jobs, self.travisName.get_text())
            s.window.show()

    def gtk_main_quit(self, widget):
        gtk.main_quit()


class ShowDialog:

    def __init__(self, markup, secondaryText):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/noUser.glade")
        self.builder.connect_signals(self)

        self.dialog = self.builder.get_object("messagedialog1")
        self.dialog.set_markup(markup)
        self.dialog.format_secondary_text(secondaryText)

    def on_backButton_clicked(self, widget):
        self.dialog.destroy()


class ShoWBuildsAndJobs():

    def __init__(self, builds, jobs, owner):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/showBuilds.glade")
        self.builder.connect_signals(self)
        self.owner = owner

        self.window = self.builder.get_object("window1")
        self.buildsTree = self.builder.get_object("treeBuildsList")
        self.jobsTree = self.builder.get_object("treeJobsList")
        self._addColumn("Repository", 0, self.buildsTree)
        self._addColumn("Build ID", 1, self.buildsTree)
        self._addColumn("Build Number", 2, self.buildsTree)
        self._addColumn("State", 3, self.buildsTree)
        self.buildsList = self.builder.get_object("buildsList")

        for elem in builds:
            self._addBuild(elem, self.buildsList)

        self._addColumn("Repository", 0, self.jobsTree)
        self._addColumn("Job ID", 1, self.jobsTree)
        self._addColumn("Job Number", 2, self.jobsTree)
        self.jobsList = self.builder.get_object("jobsList")

        for job in jobs:
            self._addJob(job, self.jobsList)


    def _addColumn(self, title, columnID, tree):
        """
        This function adds a column to the list view. First it create the gtk.
        TreeViewColumn and then set some needed properties.
        """
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text = columnID)
        column.set_resizable(True)
        column.set_sort_column_id(columnID)
        tree.append_column(column)


    def _addBuild(self, build, listview):
        """
        Add build to the tree view
        """
        listview.append([build['repository'], int(build['id']), int(build['number']), build['state']])


    def _addJob(self, job, listview):
        """
        Add a job to the tree view
        """
        listview.append([job['repository'], int(job['id']), float(job['number'])])


    def on_showBuildButton_clicked(self, widget):
        selection = self.buildsTree.get_selection()
        (model, iter) = selection.get_selected()
        #Check if there is any row selected
        if not iter:
            w = ShowDialog("Warning!", "No build selected.")
            w.dialog.show()
        else:
            buildID = model.get_value(iter, 1)
            sbl = ShowBuildLog(buildID, model.get_value(iter, 0), self.owner)
            sbl.w.show()


    def gtk_main_quit(self, widget):
        gtk.main_quit()


class ShowBuildLog:

    def __init__(self, buildID, repo, owner):
        self.builder = gtk.Builder()
        self.builder.add_from_file("UI/showBuildLog.glade")
        self.builder.connect_signals(self)

        self.w = self.builder.get_object("window1")
        self.log = self.builder.get_object("logView")
        self.logBuffer = self.builder.get_object("logBuffer")

        job = travisParser.getRelatedJob(buildID, repo, owner)
        self.logBuffer.set_text(job['log'])



if __name__ == "__main__":
    a = TravisCIUsername()
    a.mainWindow.show()
    gtk.main()