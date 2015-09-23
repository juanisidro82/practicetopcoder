nombreclase = "Time"
definicion = "whatTime"
directorio = "/home/isidro/topcoder/workspace/SRM 144"
setwd(directorio)

source(paste(nombreclase, ".R", sep=""))
library('RUnit')

tipoclases <- getSlots(nombreclase)

objecto = new(nombreclase)

testarchivo = readLines(paste(nombreclase, ".sample", sep=""))
entrada = ""
salida = ""
for (i in 1:length(testarchivo)) {
  if (substring(testarchivo[i], 1, 10) == "-- Example") {
    numeroprueba = testarchivo[i]
    entrada = testarchivo[i+1]
    salida =  testarchivo[i+3]
    texto = paste("objecto@", names(tipoclases)[1], " = ", entrada, sep ="")
    eval(parse(text=texto))
    if (checkEquals(salida, whatTime(objecto)))  {
      print(numeroprueba)
      print("passed")
    }
    else {
      print(numeroprueba)
      print("failed")
    }
  }
}


