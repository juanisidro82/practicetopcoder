library('RUnit')

tipoclases <- getSlots(nombreclase)

objecto = new(nombreclase)

testarchivo = readLines(paste(nombreclase, ".sample", sep=""))
entrada = ""
salida = ""
lineastestarchivo = length(testarchivo)
for (i in 1:lineastestarchivo) {
    if (substring(testarchivo[i], 1, 10) != "-- Example") next
    indicelineavacia = i + 1
    indicelineafin = i + 1
    while(substring(testarchivo[indicelineafin], 1, 10) != "-- Example" && indicelineafin <= lineastestarchivo) {
        if (testarchivo[indicelineafin] == "") indicelineavacia = indicelineafin
        indicelineafin = indicelineafin + 1
    }
    numeroprueba = testarchivo[i]
    entrada = testarchivo[(i+1):(indicelineavacia - 1)]
    salida =  testarchivo[(indicelineavacia + 1):(indicelineafin - 1)]
    texto = paste("objecto@", names(tipoclases)[1], " = ", entrada, sep ="")
    eval(parse(text=texto))
    resultados = eval(call(definicion, objecto))
    if (checkEquals(salida, resultados))  {
      print(numeroprueba)
      print("passed")
    }
    else {
      print(numeroprueba)
      print("failed")
    }

}


