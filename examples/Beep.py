#!/usr/bin/env python
# encoding: utf-8

from yast import *
import time

# Test for UI::Beep()
class BeepClient:
    def main(self):
      UI.OpenDialog(Label("Doing some operations..."))
      time.sleep(4)
      UI.CloseDialog()

      UI.Beep()
      UI.OpenDialog(
        VBox(
          Label("Done. Now prooceed to answer the next questions."),
          PushButton("Ok")
        )
      )
      UI.UserInput()
      UI.CloseDialog()

BeepClient().main()
