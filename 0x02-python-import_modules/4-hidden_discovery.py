if __name__ == "__main__":
    import hidden_4
    for i in dir(hiden_4):
        if not i.startswith("__"):
            print("{}".format(i))
