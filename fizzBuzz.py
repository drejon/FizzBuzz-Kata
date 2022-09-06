
def fizzBuzz(number): 
    
    if (number % 3 == 0) and (number % 5 == 0): return "FizzBuzz" 
    elif (number % 3 == 0): return "Fizz"
    elif (number % 5 == 0): return "Buzz"
    else: return number


class TestFizzBuzz():
    
    def test_fizz(self):

        list_of_numbers = list(range(1,5))
        result = []
        for numbers in list_of_numbers:
            result.append(fizzBuzz(numbers))
        
        assert result, [1, 2, "Fizz", 4]

    def test_Buzz(self):

        list_of_numbers = [5, 7, 8, 10]
        result = []
        for numbers in list_of_numbers:
            result.append(fizzBuzz(numbers))
        
        assert result, ["Buzz", 7, 8, "Buzz"]

    def test_FizzBuzz(self):
        list_of_numbers = list(range(0, 16))
        result = []
        for numbers in list_of_numbers:
            result.append(fizzBuzz(numbers))
        
        assert result, ["FizzBuzz", 1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]