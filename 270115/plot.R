#install.packages('Peptides')
library('Peptides')
library('ggplot2')
library('scales')

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
    ExportPlot(plot, "potential")
}

#pot <- read.xvg("/Volumes/Daten/documents/coding/git/MD/270115/potential.xvg")
#colnames(pot)  <-  c("time", "potential")
#str(pot)
#pot$Time (ps)
#ggplot(data=pot, aes(x=time, y=potential)) + geom_line() 
