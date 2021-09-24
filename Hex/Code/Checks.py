def check(errs: dict[str, function], args: list):
    if not any(args): # file is supplied
        errs["Melon"]()

    try: # file is valid
        open(args[1], "r").close()
    except OSError:
        errs["Domain"]()

    try: # platform supports tty
        import tty, termios
    except ModuleNotFoundError:
        errs["TTY"]()