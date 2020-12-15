#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_names = dir(hidden_4)
    for i in list_names:
        if i[1] != "_":
            print(i)
