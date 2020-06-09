''' PROGRAMMING ASSIGNMENT # 3
GENERAL DIRECTIONS:

Download the following text file:

QuickSort.txt
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the i^{th}i 
th
  row of the file gives you the i^{th}i 
th
  entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length mm, you should simply add m-1m−1 to your running total of comparisons. (This is because the pivot element is compared to each of the other m-1m−1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:

For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

HOW TO GIVE US YOUR ANSWER:

Type the numeric answer in the space provided.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.

(We do not require you to submit your code, so feel free to use the programming language of your choice, just type the numeric answer in the following space.)

1 point
Enter answer here
2.Question 2
GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

See the first question.

DIRECTIONS FOR THIS PROBLEM:

Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element. Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.

Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.

1 point
Enter answer here
3.Question 3
GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

See the first question.

DIRECTIONS FOR THIS PROBLEM:

Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule. [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k2k, use the k^{th}k 
th
  element as the "middle" element. So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.

SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements. You should NOT do this. That is, as in the previous two problems, you should simply add m-1m−1 to your running total of comparisons every time you recurse on a subarray with length mm.

Solution taken from https://pythonandr.com/2016/07/13/computing-work-done-total-pivot-comparisons-by-quick-sort/
'''

#Case 1
#First element of the unsorted array is chosen as pivot element for sorting using QuickSort

def count_pivotFirst(x):
    '''Counts number of comparisons while using Quick Sort with the first element of the unsorted array as the pivot element.''' 
    global count_pivot_first
    if len(x) ==1 or len(x) ==0:
        return x
    else:
        count_pivot_first += len(x) -1
        i = 0
        for j in range(len(x) -1):
            if x[j+1] < x[0]: #compare next element to the pivot x[0]
                x[j+1], x[i+1] = x[i+1], x[j+1] #swap the two elements if the current jth element is less than the pivot. However, note i is not incremented with every i bc the x[j+1] < x[0] term is not always true.
                i += 1 #and the i increment just comes here.
        x[0], x[i] = x[i], x[0] #is this moving the pivot point over to x[i] with every recursive call?

        first_part = count_pivotFirst(x[:i])
        second_part = count_pivotFirst(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part


#Case 2
#Last element of the unsorted array is chosen as pivot element for sorting using QuickSort

def count_pivotLast(x):
    '''Counts numbers of comparisons while using quicksort with the last element of the array as the pivot'''
    global count_pivot_last
    if len(x) ==1 or len(x) ==0:
        return x
    else:
        count_pivot_last += len(x) -1
        x[0], x[-1] = x[-1], x[0]
        i = 0
        for j in range(len(x) -1):
            if x[j+1] < x[0]: #compare next element to the pivot x[0]
                x[j+1], x[i+1] = x[i+1], x[j+1] #swap the two elements if the current jth element is less than the pivot. However, note i is not incremented with every i bc the x[j+1] < x[0] term is not always true.
                i += 1 #and the i increment just comes here.
        x[0], x[i] = x[i], x[0] #is this moving the pivot point over to x[i] with every recursive call?

        first_part = count_pivotLast(x[:i])
        second_part = count_pivotLast(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part


#Case 3
#Median-of-three method used to choose pivot element

def middle_index(x):
    '''returns the index of the middle element'''
    if len(x) %2 ==0:
        middle_index = len(x)//2 -1
    else:
        middle_index = len(x)//2
    return middle_index

def median_index(x, i, j, k):
    '''Returns the median index of three when passed an array and indices of any 3 elements of that array'''
    if (x[i] - x[j])*(x[i] - x[k]) < 0:
        return i
    elif (x[j] - x[i])*(x[j] - x[k]) < 0:
        return j
    else:
        return k


def count_pivotMid(x):
    global count_pivot_median
    if len(x) ==1 or len(x) ==0:
        return x
    else:
        count_pivot_median += len(x) -1
        k = median_index(x, 0, middle_index(x), -1) #x is input array, 0 is starting index, middle_index is middle of array, -1 is the last element of the array
        if k != 0: x[0], x[k] = x[k], x[0] #if the median index is not 0, move the element found in the median index to the front of the array and use it as the pivot for the rest of the algo.
        
        i = 0
        for j in range(len(x) -1):
            if x[j+1] < x[0]: #compare next element to the pivot x[0]
                x[j+1], x[i+1] = x[i+1], x[j+1] #swap the two elements if the current jth element is less than the pivot. However, note i is not incremented with every i bc the x[j+1] < x[0] term is not always true.
                i += 1 #and the i increment just comes here.
        x[0], x[i] = x[i], x[0] #is this moving the pivot point over to x[i] with every recursive call?

        first_part = count_pivotMid(x[:i])
        second_part = count_pivotMid(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part




#initialize the counters
count_pivot_first = 0; count_pivot_last = 0; count_pivot_median = 0

numlist_filename = r"C:\Users\numai\Documents\Learning\AlgorithmsSpecialization\DividAndConquer_StanfordClass\assignments\week3.txt"
data =[]
with open(numlist_filename, "r") as f:
    for i in f:
        data.append(int(i))

count_pivotFirst(data)

count_pivotLast(data)

count_pivotMid(data)

print(len(data))

print(count_pivot_first)
print(count_pivot_last)
print(count_pivot_median)