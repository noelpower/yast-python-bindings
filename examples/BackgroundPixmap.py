#!/usr/bin/env python
# encoding: utf-8

from yast import *

# Simple example how to use background pixmaps in alignments
class BackgroundPixmapClient:
    def main(self):
      l = List()
      l.add(String("/usr/share/wallpapers/Mountains.jpg"))
      UI.OpenDialog(
        Opt("defaultsize"),
        VBox(
          HVCenter(
            #term("BackgroundPixmap", "wallpapers/welcome.jpg"),
            Term("BackgroundPixmap", l),
            MinSize(20, 7, SelectionBox("", ["English", "Italiano", "Klingon"]))
          ),
          Right(PushButton(Opt("default"), "&Close"))
        )
      )
      UI.UserInput()
      UI.CloseDialog()

BackgroundPixmapClient().main()
