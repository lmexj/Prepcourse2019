Exploratory Data Analysis
========================================================
author: Jing Xu (Applied Bioinformatics (B330), DKFZ)
date: 2019-03-08
autosize: true
width: 1440
height: 900



Outline
========================================================
- Reading and exporting data
- Cleaning data
- Learn to use **dplyr** package
- Descriptive statistics
- Basic plotting functions


Before importing data ...
========================================================
- In regular R file, you may need to setup your working directory by `setwd("YourFilePath")`, note that you need to use __forward slash ("/")__ instead of back slash, the file path should be inside the quotation mark
- Check if your working directory is correct by `getwd()`
- Check which files or folders are in the working directory by `list.files()`
- Load necessary packages:
    + if preexisting: `library("package name")`
    + if new (depends on the resources): 
        from CRAN R package repository (main): `install.packages("package name")` or simply click "Install" button in the lower right window in R studio
    + if outdated (CRAN R package): update your package by `update.packages(package name)` or click "update" button


R packages resources
========================================================
* [The CRAN package repository](https://cran.r-project.org/web/packages/
): currently 13832 packages available
* [Bioconductor](https://www.bioconductor.org/): packages for high-throughput genomic data, currently 1649 packages


```r
if (!requireNamespace("BiocManager"))
    install.packages("BiocManager")
BiocManager::install("GenomicFeatures")
```

* Github repo: mostly unoffcial packages, under development or not intended to publish

```r
install.packages("devtools")
devtools::install_github("developername/packagename")
```


Getting data into R
========================================================
There are many ways to import data into R depending on the data format, Sometimes you need to download a specific package for reading data. Here are some commonly used functions. 

        Functions        |        File type        |  required Package
    ---------------------|-------------------------|--------------------
      `read.csv()`       |  comma separated files  |     basic
      `read.table()`     |  csv, txt, semicolon    |     basic
      `read.delim()`     |  other delimited Files  |     basic
      `readHTMLTable()`  |  HTML file (URL)        |   RCurl, XML
      `read.xls()`       |  Excel xls sheets       |     gdata 
      `read.xlsx()`      |  Excel xlsx sheets      |     openxlsx 
        
- However, things may not go as smooth as you think ... sometimes it can be very frastrating for not being able to read some xlsx sheets into R, especially when you have dirty data. 


Inspect your data 
========================================================
**It's extremely important to work with clean data!** Excel sheets always use free text boxes which may contain lots of garbage, you cannot even read the mess into R! Sometimes you can get data into R, but 

- Does it follow "one column one data type" rules? 
- In each column, do call the formats look alike? Can they be separate by regular expression?
- In each column, are all the values in correct format as required? (e.g. character format, date format, number range ...) Identify the wrong ones and try to fix them.
- Convert missing values to NA


Some examples of bad data...
========================================================
1. A column named "cell number"...

```
[1] "1970000"       "11800000"      "9.23E04 cells"
```

```
[1]  1970000 11800000       NA
```


```r
# which value is not a number?
suppressWarnings(
    cellnumber[which(is.na(as.numeric(cellnumber)))]
    )
```

```
[1] "9.23E04 cells"
```

```r
# which values are numbers?
suppressWarnings(
    cellnumber[which(!is.na(as.numeric(cellnumber)))]
    )
```

```
[1] "1970000"  "11800000"
```


=======================================================
How to fix this with R?

```r
cellnumber[which(is.na(as.numeric(cellnumber)))] <- "9.23E04"
cellnumber <- as.numeric(cellnumber)
cellnumber
```

```
[1]  1970000 11800000    92300
```

But what if there are many values like this?

```r
ind <- which(is.na(as.numeric(cellnumber)))

# method 1. string split
as.numeric(unlist(strsplit(as.character(cellnumber[ind]), " "))[1])

# method 2. string split by sapply
as.numeric(sapply(strsplit(as.character(cellnumber[ind]), " "), "[[", 1))
```
Pandoc bug... cannot display the results correctly, you can try to run it in R console.


Load build-in data sets
========================================================
Build-in data sets and external data packages are very good sources to practice R coding. You can either call them directly, or use `data()` function to get them into the console.

Some famous datasets: e.g. **iris**, **mtcars**
- The **Iris** flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in 1936. 
- The **mtcars** data set (Motor trend car road test) was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973 to 1974 models).


The Iris flower data
========================================================
- 50 samples; 3 species ( _Iris setosa_ , _Iris virginica_ and _Iris versicolor_); 4 features: the length and the width of the sepals and petals, in centimeters. 
- Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 


```r
str(iris)
```

```
'data.frame':	150 obs. of  5 variables:
 $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
 $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
 $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
 $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
 $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 1 1 1 1 1 1 1 1 1 1 ...
```


Get to know 'dplyr' for data frames
========================================================
* Selecting columns with long variables names or subset data based on multiple columns can produce lengthy code, which is very difficult to read. The 'dplyr' package provides a handful of useful functions for easy data frame manipulation:

    - `filter()` to select cases based on their values.
    - `arrange()` to reorder the cases.
    - `select()` and `rename()` to select variables based on their names.
    - `mutate()` and `transmute()` to add new variables that are functions of existing variables.
    - `summarise()` to condense multiple values to a single value.
    - `group_by()`to group data based on variable(s)

* You can pipe your code by `%>%`


Select and filter 
========================================================

```r
names(iris)
```

```
[1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width" 
[5] "Species"     
```

```r
iris[iris$Sepal.Width>4,c("Species", "Sepal.Width", "Sepal.Length")]
```

```
   Species Sepal.Width Sepal.Length
16  setosa         4.4          5.7
33  setosa         4.1          5.2
34  setosa         4.2          5.5
```


```r
# dplyr package is loaded in setup chunk
iris %>% select(Species, Sepal.Width, Sepal.Length) %>% filter(Sepal.Width>4)
```

```
  Species Sepal.Width Sepal.Length
1  setosa         4.4          5.7
2  setosa         4.1          5.2
3  setosa         4.2          5.5
```


Mutate and arrange
========================================================

```r
Data <- iris %>% 
        mutate(height= sample(seq(30.0, 50.0, by=0.2), nrow(iris), replace = T )) %>%
        filter(height > 40) %>%        
        dplyr::select(Species, Sepal.Length, Sepal.Width, height) %>% 
        arrange(height)

head(Data) 
```

```
     Species Sepal.Length Sepal.Width height
1     setosa          4.9         3.6   40.2
2 versicolor          6.3         2.5   40.4
3     setosa          5.4         3.9   40.6
4 versicolor          6.7         3.1   40.6
5     setosa          5.2         3.4   40.8
6     setosa          5.0         3.3   40.8
```



Data distribution
========================================================
Overview of total distribution by `summary()`

```
  Sepal.Length    Sepal.Width     Petal.Length    Petal.Width   
 Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100  
 1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300  
 Median :5.800   Median :3.000   Median :4.350   Median :1.300  
 Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199  
 3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800  
 Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500  
       Species  
 setosa    :50  
 versicolor:50  
 virginica :50  
                
                
                
```


========================================================

```r
par(mfrow =c(1,2))
graphics::boxplot(iris[,names(iris) != "Species"], main="Boxplot", xlab="measurement", ylab="values")
graphics::boxplot(iris[,names(iris) != "Species"], 
        main="Boxplot", xlab="measurement", ylab="values",
        col=c("red", "blue", "green", "yellow") )
```

<img src="PrepCourse_ExploratoryAnalysis-figure/unnamed-chunk-10-1.png" title="plot of chunk unnamed-chunk-10" alt="plot of chunk unnamed-chunk-10" style="display: block; margin: auto;" />



Calculation based on a variable
========================================================
* Use `tapply(vector, index, function)`

```r
tapply(iris$Sepal.Length, iris$Species, mean)
```

```
    setosa versicolor  virginica 
     5.006      5.936      6.588 
```

```r
tapply(iris$Sepal.Width, iris$Species, mean)
```

```
    setosa versicolor  virginica 
     3.428      2.770      2.974 
```

```r
tapply(iris$Petal.Length, iris$Species, mean)
```

```
    setosa versicolor  virginica 
     1.462      4.260      5.552 
```

```r
tapply(iris$Sepal.Width, iris$Species, mean)
```

```
    setosa versicolor  virginica 
     3.428      2.770      2.974 
```

========================================================
* Use `group_by` and `summarise_at` from `dplyr` package

```r
iris %>% 
    group_by(Species) %>%
    summarise(mean=mean(Sepal.Length))
```

```
# A tibble: 3 x 2
  Species     mean
  <fct>      <dbl>
1 setosa      5.01
2 versicolor  5.94
3 virginica   6.59
```


========================================================

```r
par(mfrow =c(1,2))
graphics::boxplot(iris$Sepal.Width ~ as.factor(iris$Species), 
                  col=c("red", "blue", "green")) 
graphics::boxplot(iris$Sepal.Length ~ as.factor(iris$Species), 
                  col=c("red", "blue", "green")) 
```

<img src="PrepCourse_ExploratoryAnalysis-figure/unnamed-chunk-13-1.png" title="plot of chunk unnamed-chunk-13" alt="plot of chunk unnamed-chunk-13" style="display: block; margin: auto;" />


Correlation
========================================================
Is there any correlation between these variables?
It's a good idea to plot your data first!

```r
pairs(iris)
```

<img src="PrepCourse_ExploratoryAnalysis-figure/unnamed-chunk-14-1.png" title="plot of chunk unnamed-chunk-14" alt="plot of chunk unnamed-chunk-14" style="display: block; margin: auto;" />


Test correlations
========================================================

```r
cor.test(iris$Petal.Length, iris$Sepal.Width, method="spearman")
```

```

	Spearman's rank correlation rho

data:  iris$Petal.Length and iris$Sepal.Width
S = 736640, p-value = 0.0001154
alternative hypothesis: true rho is not equal to 0
sample estimates:
       rho 
-0.3096351 
```

```r
cor.test(iris$Petal.Length, iris$Sepal.Length, method = "spearman")
```

```

	Spearman's rank correlation rho

data:  iris$Petal.Length and iris$Sepal.Length
S = 66429, p-value < 2.2e-16
alternative hypothesis: true rho is not equal to 0
sample estimates:
      rho 
0.8818981 
```

========================================================
You may also check paired correlation for all variables

```r
M <- suppressMessages(stats::cor(iris[1:4]));
M
```

```
             Sepal.Length Sepal.Width Petal.Length Petal.Width
Sepal.Length    1.0000000  -0.1175698    0.8717538   0.8179411
Sepal.Width    -0.1175698   1.0000000   -0.4284401  -0.3661259
Petal.Length    0.8717538  -0.4284401    1.0000000   0.9628654
Petal.Width     0.8179411  -0.3661259    0.9628654   1.0000000
```

========================================================
Use `corrplot` package for visulization

```r
par(mfrow =c(1,2))
corrplot(M)
corrplot(M, method = "number")
```

<img src="PrepCourse_ExploratoryAnalysis-figure/unnamed-chunk-17-1.png" title="plot of chunk unnamed-chunk-17" alt="plot of chunk unnamed-chunk-17" style="display: block; margin: auto;" />


========================================================
# $\color{red}{\text{Congrats! You finish this session!}}$
