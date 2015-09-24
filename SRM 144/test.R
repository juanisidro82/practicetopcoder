library('RUnit')

tipoclases <- getSlots(nombreclase)

objecto = new(nombreclase)

testarchivo = readLines(paste(nombreclase, ".sample", sep=""))
entrada = ""
salida = ""
for (i in 1:length(testarchivo)) {
    if (substring(testarchivo[i], 1, 10) != "-- Example") next
    numeroprueba = testarchivo[i]
    entrada = testarchivo[i+1]
    salida =  testarchivo[i+3]
    texto = paste("objecto@", names(tipoclases)[1], " = ", entrada, sep ="")
    eval(parse(text=texto))
    resultados = eval(call(definicion, objecto))
    print(resultados)
    if (checkEquals(salida, resultados))  {
      print(numeroprueba)
      print("passed")
    }
    else {
      print(numeroprueba)
      print("failed")
    }

}


