#install.packages('Peptides')
library('Peptides')
library('ggplot2')
library('scales')
library(zoo)

scientific_10 <- function(x) {
    parse(text=gsub("e", " %*% 10^", scientific_format()(x)))
}


ExportPlot <- function(gplot, filename, width=5, height=4) {
    # Export plot in PDF and EPS.
    # Notice that A4: width=11.69, height=8.27
    ggsave(paste(filename, '.pdf', sep=""), gplot, width = width, height = height)
    postscript(file = paste(filename, '.eps', sep=""), width = width, height = height)
    print(gplot)
    dev.off()
    png(file = paste(filename, '_.png', sep=""), width = width * 100, height = height * 100)
    print(gplot)
    dev.off()
}

plotPotential <- function(path, title=""){
    pot <- read.xvg(path)
    colnames(pot)  <-  c("time", "potential")
    if (title =="") {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ps)") + ylab("potential energy (kJ/mol)") + scale_y_continuous(label=scientific_10)
    } else {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ps)") + ylab("potential energy (kJ/mol)") + ggtitle(title) + scale_y_continuous(label=scientific_10)
    }
    ExportPlot(plot, tail(strsplit(path, "/")[[1]], n=1))
}


plotTemp <- function(path, title=""){
    pot <- read.xvg(path)
    colnames(pot)  <-  c("time", "potential")
    if (title =="") {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ps)") + ylab("temperature (K)") # + scale_y_continuous(label=scientific_10)
    } else {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ps)") + ylab("temperature (K)") + ggtitle(title) #+ scale_y_continuous(label=scientific_10)
    }
    ExportPlot(plot, tail(strsplit(path, "/")[[1]], n=1))
}

plotRMSD <- function(path, title=""){
    pot <- read.xvg(path)
    colnames(pot)  <-  c("time", "potential")
    if (title =="") {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ns)") + ylab("RMSD (nm)") # + scale_y_continuous(label=scientific_10)
    } else {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ns)") + ylab("RMSD (nm)") + ggtitle(title) #+ scale_y_continuous(label=scientific_10)
    }
    ExportPlot(plot, tail(strsplit(path, "/")[[1]], n=1))
}

plotGyrate <- function(path, title=""){
    pot <- read.xvg(path)
    colnames(pot)  <-  c("time", "potential")
    if (title =="") {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ps)") + ylab("radius of gyration (nm)") # + scale_y_continuous(label=scientific_10)
    } else {
        plot <- ggplot(data=pot, aes(x=time, y=potential)) + geom_line() + xlab("time (ps)") + ylab("radius of gyration (nm)") + ggtitle(title) #+ scale_y_continuous(label=scientific_10)
    }
    ExportPlot(plot, tail(strsplit(path, "/")[[1]], n=1))
}

plotPressure <- function(path, title=""){
    pot <- read.xvg(path)
    colnames(pot)  <-  c("time", "pressure")
    #Make zoo object of data
    temp.zoo<-zoo(pot$pressure,pot$time)
    #Calculate moving average with window 3 and make first and last value as NA (to ensure identical length of vectors)
    m.av<-rollmean(temp.zoo, 10,fill = list(NA, NULL, NA))
    #Add calculated moving averages to existing data frame
    pot$amb.av=coredata(m.av)
    if (title =="") {
        plot  <- ggplot(data=pot, aes(x=time, y=pressure)) + geom_line() + xlab("time (ps)") + ylab("pressure (bar)") + geom_line(aes(time,amb.av),color="red")
        #plot  <- plot + geom_line(aes(x = pot$time, y = y_sym))
    } else {
        plot <- ggplot(data=pot, aes(x=time, y=pressure)) + geom_line() + xlab("time (ps)") + ylab("pressure (bar)") + geom_line(aes(time,amb.av),color="red") + ggtitle(title) 
    }
    ExportPlot(plot, tail(strsplit(path, "/")[[1]], n=1))
}


plotDensity <- function(path, title=""){
    pot <- read.xvg(path)
    colnames(pot)  <-  c("time", "pressure")
    #Make zoo object of data
    temp.zoo<-zoo(pot$pressure,pot$time)
    #Calculate moving average with window 3 and make first and last value as NA (to ensure identical length of vectors)
    m.av<-rollmean(temp.zoo, 10,fill = list(NA, NULL, NA))
    #Add calculated moving averages to existing data frame
    pot$amb.av=coredata(m.av)
    if (title =="") {
        plot  <- ggplot(data=pot, aes(x=time, y=pressure)) + geom_line() + xlab("time (ps)") + ylab("density (kg/m^3)") + geom_line(aes(time,amb.av),color="red")
        #plot  <- plot + geom_line(aes(x = pot$time, y = y_sym))
    } else {
        plot <- ggplot(data=pot, aes(x=time, y=pressure)) + geom_line() + xlab("time (ps)") + ylab("density (kg/m^3)") + geom_line(aes(time,amb.av),color="red") + ggtitle(title) 
    }
    ExportPlot(plot, tail(strsplit(path, "/")[[1]], n=1))
}

#pot <- read.xvg("/Volumes/Daten/documents/coding/git/MD/270115/potential.xvg")
#colnames(pot)  <-  c("time", "potential")
#str(pot)
#pot$Time (ps)
#ggplot(data=pot, aes(x=time, y=potential)) + geom_line() 
