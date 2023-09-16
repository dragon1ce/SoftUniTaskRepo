def loading_bar(load):
    symbol_loaded = "%"
    symbol_loaded_not = "."
    loaded = int((load / 10))
    not_loaded = 10 - loaded
    if load == 100:
        return f"{load}% Complete!\n[{loaded * symbol_loaded}]"
    else:
        return f"{load}% [{loaded * symbol_loaded}{not_loaded * symbol_loaded_not}] \nStill loading..."


print(loading_bar(int(input())))
