def linierSequencer(var1,var2, *args):
    for function in args:
        if function(var1,var2) == False:
            return False

    else:
        return True