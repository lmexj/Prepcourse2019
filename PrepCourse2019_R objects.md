R objects
========================================================
author: Jing Xu (Applied Bioinformatics (B330), DKFZ)
date: 2019-03-08
autosize: true
width: 1440
height: 900



Outline
========================================================
- What R objects are available
- How to create each data type
- Basic functions to inspect and manipulate data


R objects (data types)
========================================================
- Everything is R is an object
- Six R data types:

    + **Vectors**: contain elements of one class, 5 types
    + **Lists**: contain elements of different classes
    + **Matrices**: vectors with 2 dimension attributes, _n_ rows x _m_ columns
    + **Arrays**: store data with > 2 dimensions. An array of dim(2,3,4) means there are 4 matrices, each with 2 rows and 3 columns.
    + **Factors**: categorical data that can be either ordered or unordered
    + **Data Frames**: most commonly used for storing tabular data, each column can be in different classes


Checking data type
========================================================
left:45%
The first step towards clean data is to know about data types. 

- Find out the data type by R function: `class()`

```r
x = c(1,2,3,"A", "B")
class(x)
```

```
[1] "character"
```

```r
x[1:2]
```

```
[1] "1" "2"
```

***
- Check data types of all columns in a data frame: `str()`

```
  Student Score     Grade
1    Jane   1.0 Very good
2    Nick   2.3      Good
```

```
'data.frame':	2 obs. of  3 variables:
 $ Student: chr  "Jane" "Nick"
 $ Score  : num  1 2.3
 $ Grade  : chr  "Very good" "Good"
```


Vectors
========================================================
- A vector can only contain obejcts of the same classes! If not, _coercion_ occurs, which may affect your analysis in later steps  
    + **character**: "Name", "Grade" ... 
    + **numeric**: real numbers, 1.6, 4, 50, -1, -20.8 ...
    + **integer**: 1L, 2L ...
    + **logical**: TRUE/FALSE
    + **complex**: mixed data type

- To check for a specific data type: `is.numeric()`, `is.integer()`, `is.factor()`, `is.character()` , `is.matrix()`  
- Convert a vector to a different data type: `as.numeric()`, `as.character()`, `as.factor()`


Create numeric & integer vectors 
========================================================
- use function `c` to create integer values, "c" stands for "combine"

```r
x <- c(1:5); x; 
```

```
[1] 1 2 3 4 5
```

```r
class(x)
```

```
[1] "integer"
```

```r
is.numeric(x)
```

```
[1] TRUE
```

***
- manual input all numbers in a vector

```r
y <- c(1,2,3,4,5); y;
```

```
[1] 1 2 3 4 5
```

```r
class(y)
```

```
[1] "numeric"
```

```r
is.integer(y)
```

```
[1] FALSE
```


Create numeric & integer vectors3
========================================================
title: false
R provides a number of functions to create a numeric vector to fit your needs:
- Create sequences

```r
seq(1,5) # the same as 1:5
```

```
[1] 1 2 3 4 5
```

```r
seq(1,3, by=0.2)
```

```
 [1] 1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6 2.8 3.0
```
__Task__: How to create an odd number series between 1 to 10 by `seq()`?

***
- Create random numbers

```r
sample(1:100,10)#random sampling from given numbers
```

```
 [1] 98 31 58 76 36 27 41 32 34  2
```

```r
rnorm(5,mean=50, sd=1) #random generation for the normal distribution
```

```
[1] 50.44971 50.82806 51.33903 49.40410 50.33057
```
__Task__: run this code for 5 times, do you get the same numbers?

Create numeric & integer vectors3
========================================================
title:false
incremental: true

It's also possible to replicate the elements by function `rep()` 

```r
rep(1:3, 3)
```

```
[1] 1 2 3 1 2 3 1 2 3
```

```r
rep(1:3, each=3)
```

```
[1] 1 1 1 2 2 2 3 3 3
```

> - __Task:__ Check the **help** page of the function to find out:  
    - How to replicate a numeric vector of '111222333' for 3 times?  
    - How to get a vector of '1223334444'?


```r
rep(1:3, each=3, times=3)
rep(1:3, c(1,2,3,4))
```


Create character vectors
========================================================
left: 60%
- Use quotation marks

```r
x <- c("male","female","male");x
```

```
[1] "male"   "female" "male"  
```

```r
x <- c("1","2","3")
y <- as.character(seq(1:3))
```

- Are x and y exactly the same?

```r
x==y
```

```
[1] TRUE TRUE TRUE
```

***
However, if you convert something that R cannot understand:

```r
x <- c("1","2","3")
as.logical(x)
```

```
[1] NA NA NA
```

```r
x <- as.numeric(x)
as.logical(x)
```

```
[1] TRUE TRUE TRUE
```


Create factors 
========================================================
- Factors are used for categorical values in either unordered or ordered way. The order can be specified by parameter `level`  
- Factors can be required for some graphical and statisitcal funtions like `lm`, where the 1st level is the baseline level 

```r
factor(c("male","female","female"))
```

```
[1] male   female female
Levels: female male
```

```r
factor(c("male","female","female"), levels = c("male", "female"))
```

```
[1] male   female female
Levels: male female
```

Some tips to deal with factors
========================================================
- Sometimes, you only want to a character vector, but by default

    + `read.table()` function reads data as factors 
    + `data.frame()` function also treats all characters vectors as factors    

    --> specify `stringsAsFactors=F` when calling the functions
***
- factor labels are recommended to use as they are self-describing

```r
Note1 <- factor(c(1.0,1.3, 1.5, 1.7,2.0));Note1 
```

```
[1] 1   1.3 1.5 1.7 2  
Levels: 1 1.3 1.5 1.7 2
```

```r
Note2 = factor(c(1.0,1.3, 1.5, 1.7,2.0), labels = c("Magna","Magna","Magna", "Gut", "Gut"));Note2
```

```
[1] Magna Magna Magna Gut   Gut  
Levels: Magna Gut
```

========================================================

```r
par(mfrow=c(1,2))
plot(Note1, main="factor with numbers")
plot(Note2, main="factor with labels" )
```

<img src="PrepCourse2019_R objects-figure/unnamed-chunk-14-1.png" title="plot of chunk unnamed-chunk-14" alt="plot of chunk unnamed-chunk-14" style="display: block; margin: auto;" />


Missing values
========================================================
- Missing values are denoted by NA ("Not Available") or NaN ("Not a Number")
- Use `is.na()` and `is.nan()` to identify missing values
- `is.na()` returns TRUE for both NA and NaN, however `is.nan()` return TRUE for NaN (0/0) and FALSE for NA.
- Use `which()` function to get indices in the vector
- There are many reasons to have NAs, therefore it's very important to check them in your data.

***

```r
x <- c(1,2, NA,10, 20,NA, 50)
is.na(x)
```

```
[1] FALSE FALSE  TRUE FALSE FALSE  TRUE FALSE
```

```r
which(is.na(x))
```

```
[1] 3 6
```

```r
# how many NAs do we have?
sum(is.na(x)) 
```

```
[1] 2
```


========================================================
- Sometimes we need to omit NAs for data processing, since we want to get a complete dataset

```r
complete.cases(x)
```

```
[1]  TRUE  TRUE FALSE  TRUE  TRUE FALSE  TRUE
```

```r
x[complete.cases(x)]
```

```
[1]  1  2 10 20 50
```

```r
length(x[complete.cases(x)])
```

```
[1] 5
```

***
- Many mathematical functions do not work if there is a NA, e.g. `max()`

```r
max(x)
```

```
[1] NA
```

```r
max(x, na.rm = T)
```

```
[1] 50
```
__Task__: 1. How to deselect elements? 2. Try other mathematical functions, what if we want to know the mininum, the mean, the median and total sum of x?


Create matrices
========================================================
- Matrix has two dimensions: No. of rows and No. of columns, try `dim()` and `attributes()`
- Matrix can be used interchangeably with data frame, when a data frame only contain numbers. Some graphical functions require input data to be a matrix, e.g. `heatmap()`. 

```r
x = matrix(data=1:15, nrow = 3,ncol = 5, byrow = T); x
```

```
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    2    3    4    5
[2,]    6    7    8    9   10
[3,]   11   12   13   14   15
```

```r
dim(x) 
```

```
[1] 3 5
```

========================================================

```r
# You can specify row names and column names for a matrix
dimnames(x) <- list(c("r1","r2","r3"),paste("c",seq(1:5), sep=""));x
```

```
   c1 c2 c3 c4 c5
r1  1  2  3  4  5
r2  6  7  8  9 10
r3 11 12 13 14 15
```

```r
attributes(x)
```

```
$dim
[1] 3 5

$dimnames
$dimnames[[1]]
[1] "r1" "r2" "r3"

$dimnames[[2]]
[1] "c1" "c2" "c3" "c4" "c5"
```


Create data frames 1
========================================================
left:55%
- Data frame can include many vectors in different classes as columns
- Create a data frame with `data.frame` function, and give meaningful variable (colnames) names!
- Basic functions in combining data

|Functions |Explanation           |Example               |
|:---------|:---------------------|:---------------------|
|c()       |combine values        |c(1,2,3)              |
|cbind     |column bind           |cbind(col1,col2,col3) |
|rbind     |row bind              |rbind(row1,row2,row3) |
|merge()   |merge two dafa frames |merge(df1,df2)        |

***
- Basic functions in inspecting data frames

|Functions |Explanation                        |Example       |
|:---------|:----------------------------------|:-------------|
|head()    |display the first 6 rows (default) |head(df)      |
|names()   |show all column names              |names(df)     |
|ncol()    |number of columns                  |ncol(df)      |
|nrows     |number of rows                     |nrows(df)     |
|$         |extract column                     |df$col1       |
|df[n,]    |extract rows                       |df[1:3,]      |
|df[,m]    |extract columns                    |df[,c(1,4,6)] |
|df[n,m]   |extract position                   |df[2,8]       |


Create data frames -- Shopping list
========================================================
Let's organize an afternoon get-together with your classmates! You have 80-Euro budget! You need to note down _items_, _price_ and _quantity_ for shopping. You may also take some _notes_ of the unit of each item. You need to keep the total cost below budget. 
- A data frame can be created as a whole or added by rows or columns 
- Calculation based on columns is also possible

```r
Item = c("instant coffee", "milk", "black tee", "cake", 
         "cookies", "orange","banana")
Price = c(4.99, 0.6, 2.42, 26, 2.2, 2.3, 2.7)
Quantity = c(1, 2, 2, 2, 2, 3, 3)
Notes = c("1 bottle", "1 litter", "20 bags", "8 inches", 
               "1 box", "1 kg","1 kg")
shopping <- data.frame(Item, Price, Notes, Quantity, stringsAsFactors = F)
shopping$Fee = shopping$Price * shopping$Quantity
```

========================================================

```r
shopping 
```

```
            Item Price    Notes Quantity   Fee
1 instant coffee  4.99 1 bottle        1  4.99
2           milk  0.60 1 litter        2  1.20
3      black tee  2.42  20 bags        2  4.84
4           cake 26.00 8 inches        2 52.00
5        cookies  2.20    1 box        2  4.40
6         orange  2.30     1 kg        3  6.90
7         banana  2.70     1 kg        3  8.10
```

```r
totalcost = sum(shopping$Fee);
totalcost 
```

```
[1] 82.43
```
You can ask R to "tell" you whether the cost is above 80 or not by control flow (we will introduce that later).

========================================================
Create a control flow by `ifelse`

```r
if (totalcost < 80){
    print(paste("It costs", totalcost, "Euros, happy shopping!", sep=" "))
} else {
    print(paste(totalcost, "Euros will be over budget, adjust your shopping list"), sep=" ")
}
```

```
[1] "82.43 Euros will be over budget, adjust your shopping list"
```
> - Curious about the `print`, `paste` functions? Check the help page! 

We are only slightly over budge, we may reduce the amount of banana from 3 kg to 2 kg. We need to change the quantity for bananas only. There are many different ways to do this:


Data manipulation in data frame
========================================================

```r
# method 1, manually count the data to see the position of the number 
shopping[7,4] <- 2 # df[row number, column number]

# method 2, ask R for the location of the number 
shopping[which(shopping$Item=="banana"), which(names(shopping)=="Quantity")] <- 2 

# method 3, re-define the whole Quantity vector
Quantity = c(1,2,2, 2,2,3,2) 

# method 4, go into Quantity column, and filter for banana
shopping$Quantity[shopping$Item=="banana"] <- 2

# method 5, go into row of banana, and filter for Quantity
shopping[shopping$Item=="banana", "Quantity"] <- 2
```
**Note**: Try to avoid any manual checking steps, if anything changes, your code won't work any more! 


========================================================
Now we need to re-calculate the total cost

```r
totalcost = sum(shopping$Price * shopping$Quantity)
if ((totalcost) < 80){
    print(paste("It costs", totalcost, "Euros, happy shopping!", sep=" "))
} else {
    print(paste(totalcost, "Euros will be over budget, adjust your shopping list"), sep=" ")
}
```

```
[1] "It costs 79.73 Euros, happy shopping!"
```


Create lists
========================================================
- Lists may include elements in different data types
- List is not very easy to handle, but it can be powerful in batch processing in combination with `apply` functions

```r
x = list(mark= c("A", "B", "C"), num= c(1,2), ID=matrix(1:4,nrow=2,ncol=2))
x
```

```
$mark
[1] "A" "B" "C"

$num
[1] 1 2

$ID
     [,1] [,2]
[1,]    1    3
[2,]    2    4
```

========================================================
- List can be named or unnamed, basic functions for lists are similar to DF, only indexing is a little different
- Access elements in a list by `[]` and `[[]]`

```r
names(x)[2]
```

```
[1] "num"
```

```r
x[1]; class(x[1])
```

```
$mark
[1] "A" "B" "C"
```

```
[1] "list"
```

***

```r
x[[2]];class(x[[2]])
```

```
[1] 1 2
```

```
[1] "numeric"
```

```r
x[[3]][1,]
```

```
[1] 1 3
```

```r
x[[3]][1] == x[[c(3,1)]]
```

```
[1] TRUE
```
__Task__: What is the output of last line? How to extract the first two elements from this list?


========================================================
# $\color{red}{\text{Congrats! You finish this session!}}$

