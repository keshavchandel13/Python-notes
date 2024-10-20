def func_1():
    loc_var = "local in function 1"
    var_1 ="var in function 1"
    def func_2():
        nonlocal loc_var 
        loc_var= "local in function 2"
        var_2 = "var in function 2"

        def func_3():
            global loc_var
            loc_var = "global in function 3"
            var_3 = "var in function 3"
            print(f"Inside func_3: loc_var = {loc_var}, var_3 = {var_3}")

        func_3()
        print(f"Inside func_2 after func_3: loc_var = {loc_var}, var_2 = {var_2}")

    func_2()
    print(f"Inside func_1 after func_2: loc_var = {loc_var}, var_1 = {var_1}")

func_1()
print(f"Outside all functions: loc_var = {loc_var}")


