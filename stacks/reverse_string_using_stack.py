"""
Reverse a given string using stack

Steps:
1. Create a stack
2. Append the element to the stack
3. Pop the element from the stack
4. Perform the string concatination


Example Test Case

Input: welcome
Output: emoclew

"""


# Push the element to the stack
def pushElement(stack, element):
	stack.append(element)
	
# Pop the element from the stack
def popElement(stack, length):
	if length == 0: 
	    return
	return stack.pop()

# Reverse the given the string
def reverseString(string):
	length = len(string)
	
	stack = []
	for i in range(0, length):
		pushElement(stack, string[i])

	reversedString = ""
	for i in range(0, length):
		reversedString += popElement(stack, length)
		
	return reversedString
	
	
if __name__ == '__main__':	
    string = "WelcomeToHacktoberfest"
    string = reverseString(string)
    print("The Reversed string is " + string)

