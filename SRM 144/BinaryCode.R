setClass("BinaryCode", representation(mensaje="character"))
setGeneric("decode", function(x) attributes(x))
setMethod("decode", "BinaryCode",
          function(x) {
            mensaje = strsplit(x@mensaje, split="")[[1]]
            n = length(mensaje)
            resultados = list(rep(0,n), rep(0, n))
            for(i in 1:2){
                if(n==1 & (as.integer(mensaje[1]) != (i - 1))) {
                    resultados[i] = "NONE"
                    next
                }
                resultados[[i]][1] = i - 1
                for (j in 1:n) {
                    if(j == 1) next
                    resultados[[i]][j] = as.integer(mensaje[j - 1]) - resultados[[i]][j - 1]
                    if (j > 2) {
                        resultados[[i]][j] = resultados[[i]][j] -  resultados[[i]][j - 2]
                    }
                    if (resultados[[i]][j] < 0 | resultados[[i]][j] > 1){
                        resultados[i] = "NONE"
                        break
                    }
                    if(as.integer(mensaje[j]) < resultados[[i]][j -1] + resultados[[i]][j]) {
                        resultados[i] = "NONE"
                        break
                    }
                }
            }
            resultados2 = c()
            for(i in 1:length(resultados)) {
                print("checar")
                resultado = resultados[[i]]
                resultados2[i] = paste(resultado, collapse="")
            }
            return(resultados2)
          }
)

nombreclase = "BinaryCode"
definicion = "decode"
directorio = "~/topcoder/practicetopcoder/SRM 144"
setwd(directorio)
source("test.R")