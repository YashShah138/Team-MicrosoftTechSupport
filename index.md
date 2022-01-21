# Midterm Vocab

## Binary Hexadecimal, Bit, Nibble, Byte
![image](https://www.watelectronics.com/wp-content/uploads/Hexadecimal-and-Binary-Number-System-Representation.jpg)
### Binary
* Binary is a number system based off of a base of 2
  * This means that the digits are powers of 2

### Hexadecimal
* Hexadecimal is a number system based off of a base of 16
  * This would be "0" through "9" and "A" through "F"
* Hexadecimal is used for hex color codes and we can pack more information
* We can express any number from 0 to 255 with just 2 digits
  * To do the same with binary, we would need 8 digits.

### Bit, Nibble, Byte
![image](https://www.dataunitconverter.com/blog/images/bit-nibble-byte-1.png)
* A bit is one binary digit
* A nibble is four bits
* A byte is eight bits

## Data, Data Abstraction
### Data
![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReAlES1HWaSRCx-0JZlJZ2iQNiZStQ0HCjkQ&usqp=CAU)
* Data is any information that can be processed and interpreted by a computer
* Almost anything can be data (or turned into data)
  * Music
  * Texts sent to a friend
  * Or a the contacts in your phone

### Data Abstraction
* Data abstraction makes data more easily read and/or understood
* For example, a computer can take a string of bits and convert them to our alphanumeric system and then display that
  * This would be like sending a set of texts

## Lossless/Lossy Compression
![image](http://pediaa.com/wp-content/uploads/2018/08/Difference-Between-Lossy-and-Lossless-Compression-Comparison-Summary.jpg)
* Lossless is used for when you cannot compromise on the quality of the message you are sending
  * Usually used with images
* Lossy is when you can compromise on the quality of the message.
  * Usually used with audio and video

## Metadata
* Metadata is information about other types of information
  * This could be:
   * the author, date, location, and time when a picture was taken
  * Or it could be how it was compressed and the original size

## Example
![San Diego SkyLine](https://user-images.githubusercontent.com/89223735/150541637-5378c5d5-7372-4a66-8294-7bc87fce7110.jpeg)
* Jan 15, 5:31 PM
* 1.04 MB
* Coronado Ferry Landing, Coronado, CA, USA
* F1.8
* 1/24 s
* 5.40 mm
* ISO 500
* No flash

## Computer Network, Parallel/Distributed Computing
### Computer Network
* A computer network is a set of computers sharing resources located on or provided by network nodes
* There are four types of computer network
  * LAN (Local Area Network)
  * PAN(Personal Area Network)
  * MAN(Metropolitan Area Network)
  * WAN(Wide Area Network)

![image](https://www.tutorialandexample.com/wp-content/uploads/2019/09/Computer-Network-1.png)

### Parallel and Distributed Computing
#### Parallel Computing
* It is a computational method where tasks are separated into operations where the are done sequentially
* Parallel computing is best for tasks that are independent of each other
  * This way they can be done simultaneously
* The time it takes for execution is the time for the longest task

#### Distributed Computing
* Uses multiple devices to complete tasks and run a program
* Solve problems that couldn’t be solved on a single computer due to processing time/storage
* Requires a network and multiple devices
* The time is takes for execution is all the times combined

## Protocol, TCP/IP, HTTP, GET, POST


## Library, Dependencies, Import


## Web API, REST, FETCH, Async, Request, Response


## Blueprints


## MVC


## Code Sequence, Procedures/Functions, Procedural Abstraction
### Code Sequence
A set of computer instructions that are executed in a logical order. Depending on the language, code sequences are either interpreted or compiled then executed. Compiled lines of code are expected to run faster than interpreted languages. Interpreted languages like Python and Javascript are converted to byte code before being executed.

### Procedures
In object-oriented languages like C++ these are called methods. In functional programming languages, they are often called functions. A good procedure is used to perform a single behavior that makes code easier to understand, test, and maintain While not desirable, a procedure can be used to run any code sequence of lengthy and unrelated steps

- - - -

Example where same procedure is called with another procedure passed as a variable argument depending on whether we use the any match or all match algorithm
```
sortBestBeaches(anyBeachCriteriaCanMatch, 'surf', 'bonfires')
sortBestBeaches(allBeachCriteriaMustMatch, 'surf', 'bonfires')
```
### Procedural Abstraction
Creating logical abstractions in code can enable greater re-use of the individual method behaviors. Procedural abstractions may take a variable number of arguments, as I did in my Favorite Beach example below. Procedural abstraction may also include abstracting the procedure itself, which I also used in my second example from my assignment below where I abstract the search method.

- - - -
```
def sortBestBeaches(match, *argv):
    best_beaches = []
    print("\nBeach Criteria", argv)
    sorted_beach_spots = sorted(local_beach_features, key=attrgetter(*argv), reverse=True)
    k = 0
    while k < len(sorted_beach_spots):
        bestspot = sorted_beach_spots[k]
        k = k + 1
        if (match(bestspot, *argv) == True):
            best_beaches.append(bestspot.__getattribute__("beach"))
            print("\r", bestspot)
    return best_beaches
```

## OOP, Class, Attribute, Method, Object
### Object-Oriented Programming
![image](https://user-images.githubusercontent.com/89176673/150482982-7ecf6054-2bf7-46d8-a58b-20ed2d4964c9.PNG)
Grady Booch defined OOP as “a method of implementation in which programs are organized as cooperative collections of objects, each of which represents an instance of some class, and whose classes are all members of a hierarchy of classes united via inheritance relationships” I would say OOP allows collections of related objects to perform business functions of value to customers. Those classes are best related to each other loosely, avoiding strong coupling such as inheritance. Ideally OOP class interactions are achieved through abstract interfaces. OOP was considered an improvement (i.e. C++) over earlier functional programming approaches such as C.

### Class
A class consists of data members and methods. Most classes are initialized through a constructor method, that may take arguments. In python init performs the object construction for a class. Data members may be initialized in the constructor, they may be initialized in the scope of the Class itself, or initialization may be delayed until later (lazy initialization) Classes allow for different access to methods and data, such as public availability to everyone and private which hides information from anyone outside the class. Best practice states we should hide implementation details inside the class that others outside do not need to know to use the class.

### Method
A method is a procedure contained within a class. Public methods can be called on instance objects of the class. Private methods can only be called within the class itself.

### Objects
In order to use a class, we need to initialize it in the form of objects. In some languages a class can be an abstract class that is not initialized, but used as a base class from which other classes can inherit. For example, an abstract Car class from which an SUV class inherits behavior. A singleton is a special class that has only one object which gets shared.

## CRUD
### Create, Read, Update, Delete
Generally speaking CRUD operations refer to input and output activities with a device such as file storage or a database. In HTTP web actions, the GET (read), PUT (create and update), and DELETE (delete) methods are also CRUD operations. Examples of each case are described below.

#### Create
An example of a Create operation would be creating a new file in the file system, or creating a new table in a database. HTTP PUT where nothing exists

#### Read
Reading input from a file in a file system. Performing a database query such as using a SQL SELECT HTTP GET

#### Update
Appending to the end of a file Performing a SQL UPDATE on a database HTTP PUT

#### Delete
Deleting portions of a file or an entire file Performing a SQL DELETE on a database HTTP DELETE

## Sort, Search-Linear/Binary
### Linear Searching
A Linear Search is also called a brute force search because it involves traversing a data structure from start to finish until the item being searched for is found. The traditional method of performing such a search is using a looping mechanism, but modern languages support lambda operations that make code more simple to read and maintain but are said to run slower. Unless the list of data items is short a linear search should not be used.

Example of an ugly linear search:
```
# Searching listOfStuff sequentially  
for i in range(0, n):  
    if (listOfStuff[i] == key):  
        return i  
return -1
```
### Binary Searching
The binary search works by repeatedly dividing up in half the portion of the list that might contain the search item, until we have just one place left to check (the thing we want to find). This is at the worst case Log n number of searches to find our item in a sorted list. A binary search only works if the data is sorted. For larger data sets, sort the data, then use binary search. In Python 3.10 we can use containers that automatically work as ordered so we can just use binary search. I learned recently that older versions of Python behaved differently and some structures were unordered.

- - - -

Example of a binary search using recursion (shorter code) in Python
```
if high >= low:

    mid = low + (high - low)//2

    # If found at mid, then return it
    if array[mid] == x:
        return mid

    # Search the left half
    elif array[mid] > x:
        return binarySearch(array, x, low, mid-1)

    # Search the right half
    else:
        return binarySearch(array, x, mid + 1, high)

else:
    return -1
```
array = [3, 4, 5, 6, 7, 8, 9] x = 7

result = binarySearch(array, x, 0, len(array)-1)

if result ! = -1: print("Found it " + str(result)) else: print("Not found")
