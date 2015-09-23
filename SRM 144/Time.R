setClass("Time", representation(seconds="numeric"))
setGeneric("whatTime", function(x) attributes(x))
setMethod("whatTime", "Time",
          function(x) {
            seconds = x@seconds
            hours = seconds %/% 3600
            seconds = seconds - hours * 3600
            minutes = seconds %/% 60
            seconds = seconds - minutes * 60
            timescreen = paste(hours, ":", minutes, ":", seconds, sep = "")
            return(timescreen)
          }
)

