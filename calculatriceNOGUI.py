def calculunique():
    var1 = input('write a number : ')
    var2 = input('write the operator version python : ')
    var3 = input('write the second number of the operation : ')

    if var2 == '+': #addition
        var4 == var1 + var3
        sum(var1, var3)
        print(var4)
    if var2 == '-': #soustraction
        var4 = var1 - var3
        print(var4)        
    if var2 == '*': #multiplication 
        var4 = var1 * var3
        print(var4)        
    if var2 == '/': #division
        var4 = var1 / var3
        print(var4)        
    if var2 == '%': #modulo
        var4 = var1 % var3
        print(var4)        
    if var2 == '//': #division enttiere
        var4 = var1 // var3
        print(var4)        
    if var2 == '**': # puissance
        var4 = var1 ** var3
        print(var4)        

calculunique()
