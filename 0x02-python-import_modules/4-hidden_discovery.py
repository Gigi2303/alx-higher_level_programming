#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for g in dir(hidden_4):
        if g.startswith("__"):
            continue
        else:
            print(g)
