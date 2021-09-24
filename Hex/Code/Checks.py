

# Definitions
class check:
    def __init__(self, errs: dict[str, function]):
        self.errs = errs

        self.errs.update()

    def args(self, args: list):
        if not any(args): # file is supplied
            self.errs["Melon"]()
        else:
            try: # file is valid
                if args != None:
                    open(args[1], "r").close()
            except OSError:
                self.errs["Domain"]()

    def tty(self):
        try: # platform supports tty
            import tty, termios
        except ModuleNotFoundError:
            self.errs["TTY"]()


# Runtime