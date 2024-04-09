

conjunto1={1,3,5,7}
conjunto2={2,4,8}

#verificar si es un subconjunto
resultado= conjunto2.issubset(conjunto1)

#verificar si es un superconjunto
resultado= conjunto2.issuperset(conjunto1)

#verificar si hay algun numero en comun
resultado=conjunto2.isdisjoint(conjunto1)

print(resultado)
