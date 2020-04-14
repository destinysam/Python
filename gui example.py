from tkinter import *

class messagebox(gtk.dialog):
    def __init__(self, message="", buttons=(), pixmap = None, modal=True):
        gtk.dialog.__init__(self)
        self.connect("destroy", self.quit)
        self.connect("delete_event", self.quit)
        if modal:
            self.set_modal(True)
        hbox = gtk.Hbox(spacing=5)
        hbox.set_border_width(5)
        self.vbox.pack_start(hbox)
        hbox.show()
        if pixmap:
            self.realize()
            pixmap = pixmap(self, pixmap)
            hbox.pack_start(pixmap, expand=False)
            pixmap.show()
            label = gtk.label(message)
            hbox.pack_start(label)
            label.show()
            for text in buttons:
                b = gtk.button(text)
                b.set_flags(gtk.CAN_DEFAULT)
                b.set_data("user_data", text)
                b.connect("clicked", self.click)
                self.action_area.pack_start(b)
                b.show()
                self.ret = None

            def quit(self, *args):
                self.hide()
                self.destroy()
                gtk.main_quit()

            def click(self, button):
                self.ret = button.get_data("user_data")
                self.quit()

            def message_box(title="message box", message="", buttons=(), pixmap=None, model=True):
                win = messagebox(message, buttons, pixmap=pixmap, modal=modal)
                win.set_title(title)
                win.show()
                gtk.main()
                return win.ret

            def test():
                result = message_box(title="test # 1", message="here is your message", buttons=("ok", "cancel"))
                print("result:", result)

            USAGE_TEXT = """
usage:
python simple_dialog.py [options]
options:
-h, --hlep display this help message.
example:
python simple.dialog.py
"""

            def usage():
                print(USAGE_TEXT)
                sys.exit(-1)

            def main():
                args = sys.argv[1:]
                try:
                    opts, args = getopt.getopt(args, "h", ["help"])
                except:
                    usage()
                    relink = 1
                    for opt, val in opts:
                        if opt in ("-h", "--help"):
                            usage()
                    if len(args) != 0:
                        usage()
                    test()

            if __name__ == "__main__":
                # import pdb; pdb.set_trace()
                main()


