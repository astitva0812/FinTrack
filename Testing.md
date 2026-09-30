# Testing - FinTrack

## 1. Testing Approach

FinTrack was tested by running the program with different users,
transaction values, and menu options.

The testing focused on checking whether the main input, storage,
viewing, and financial calculation operations produced the expected
results.

------------------------------------------------------------------------

## 2. Test Cases

  --------------------------------------------------------------------------
  Test ID        Feature Tested Input / Action Expected       Result
                                               Result         
  -------------- -------------- -------------- -------------- --------------
  T01            Add Expense    Food, 300,     Transaction is Passed
                                expense        added and      
                                               saved          

  T02            Add Income     Salary, 20000, Transaction is Passed
                                income         added and      
                                               saved          

  T03            View           Select option  Previously     Passed
                 Transactions   2              stored         
                                               transactions   
                                               are displayed  

  T04            Different User User `Aryan`,  Transaction is Passed
                                Food, 200,     saved for the  
                                expense        selected user  

  T05            Financial      Select option  Total income,  Passed
                 Summary        7              expense and    
                                               net balance    
                                               are calculated 
  --------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Test Evidence

### T01 - Add Expense

The program was tested by adding:

``` text
Category: Food
Amount: 300
Type: expense
```

The program displayed:

``` text
Added and saved!
```

![Test 1 - Add Expense](RunTest%20Pic1.png)

------------------------------------------------------------------------

### T02 - Add Income

The program was tested by adding:

``` text
Category: Salary
Amount: 20000
Type: income
```

The program displayed:

``` text
Added and saved!
```

![Test 2 - Add Income](RunTest%20Pic1.png)

------------------------------------------------------------------------

### T03 - View Transactions

After adding transactions, option 2 was selected.

The program displayed:

``` text
Food - 300 - expense
Salary - 20000 - income
```

This verifies that previously stored transactions can be retrieved and
displayed.

![Test 3 - View Transactions](RunTest%20Pic2.png)

------------------------------------------------------------------------

### T04 - Different User

The program was tested with another username.

The following transaction was entered:

``` text
Food - 200 - expense
```

The program displayed:

``` text
Added and saved!
```

This demonstrates that transactions can be recorded under different
usernames.

![Test 4 - Different User](RunTest%20Pic3.png)

------------------------------------------------------------------------

### T05 - Financial Summary

The financial summary feature was tested using option 7.

The program displayed:

``` text
Total income: 0
Total expense: 6000
Net balance: -6000.0
```

The result follows:

``` text
Net Balance = Total Income - Total Expense
            = 0 - 6000
            = -6000
```

![Test 5 - Financial Summary](RunTest%20Pic4.png)

------------------------------------------------------------------------

## 4. Additional Features Requiring Testing

The program also contains the following features:

-   Finding the highest expense
-   Reversing transactions
-   Removing duplicate transactions
-   Separating income and expenses
-   Counting transactions
-   Counting income and expense transactions
-   Finding unique categories
-   Finding the Kth smallest expense
-   Invalid input handling
-   Exiting the program

These features are implemented in the program but were not included in
the available screenshot evidence.

They should be tested separately if additional testing time is
available.

------------------------------------------------------------------------

## 5. Testing Summary

The available test evidence demonstrates successful execution of:

-   Adding expense transactions
-   Adding income transactions
-   Viewing stored transactions
-   Recording transactions for different users
-   Calculating total income
-   Calculating total expenses
-   Calculating net balance

The testing evidence is based on actual program executions and
screenshots included in the repository.
