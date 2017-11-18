# encoding: utf-8

from yast import *
class Table6MultiSelClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          Heading("Today's menu"),
          MinSize(
            30,
            10,
            Table(
              Id("menu"),
              Opt("multiSelection"),
              Header("Name", "Price"),
              [
                Item(Id('1'), "Chili", 6),
                Item(Id('2'), "Salami Baguette", Void()),
                Item(Id('3'), "Spaghetti", 8),
                Item(Id('4'), "Steak Sandwich", 12)
              ]
            )
          ),
          PushButton("&OK")
        )
      )

      UI.ChangeWidget("menu", "SelectedItems", [Id('1'), Id('2')])

      UI.UserInput()

      sel = UI.QueryWidget("menu", "SelectedItems")
      UI.CloseDialog()

      ycpbuiltins.y2milestone("Selected: %1", sel)


Table6MultiSelClient().main()
