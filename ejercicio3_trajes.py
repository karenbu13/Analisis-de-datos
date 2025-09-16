cantidad_traje=0; preciou=0; subtotal=0;dto=0;total=0

cantidad_traje=int(input("por favor ingrese cantidad de trajes"));
preciou=int(input("por favor ingrese precio unitario"))

if(cantidad_traje==1):
    subtotal=(preciou*cantidad_traje)
    dto=(subtotal*0.50)
    total=(subtotal-dto)
    print("subtotal a pagar",subtotal)
    print("dto es", dto) 
    print("total a pagar es",total)


if(cantidad_traje==2):
    subtotal=(preciou*cantidad_traje)
    dto=(subtotal*0.55)
    total=(subtotal-dto)
    print("subtotal a pagar",subtotal)
    print("dto es", dto) 
    print("total a pagar es",total)

    

if(cantidad_traje==3):
    subtotal=(preciou*cantidad_traje)
    dto=(subtotal*0.60)
    total=(subtotal-dto)
    print("subtotal a pagar",subtotal)
    print("dto es", dto) 
    print("total a pagar es",total)

if(cantidad_traje>3):
    subtotal=(preciou*cantidad_traje)
    dto=(subtotal*0.65)
    total=(subtotal-dto)
    print("subtotal a pagar",subtotal)
    print("dto es", dto) 
    print("total a pagar es",total)

