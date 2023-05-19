def print_data_type(func):
     def wrapper(data):
          data_type = type(data).__name__
          print(f'Data_type:{data_type}')
          return func(data)
     return wrapper

@print_data_type
def function(data):
     if isinstance(data,tuple):
        len_str = sum(len(str(item)) for item in data if isinstance(item,str))
        print(f'Общая длина всех строк: {len_str}')
     elif isinstance(data,list):
        total_letters = sum(len(str(item)) for item in data if isinstance(item,str))
        total_numbers = sum(len(str(item)) for  item in data if isinstance(item, int) or isinstance(item,float))
        print(f'Количество букв: {total_letters}, количество чисел: {total_numbers}')
     elif isinstance(data,int):
        odd_digit_count = sum(1 for digit in str(data) if int(digit)%2!=0)
        print(f'Количество нечетных цифр: {odd_digit_count}')
     elif isinstance(data,str):
        letter_count = sum(1 for letter in data if letter.isalpha())
        print(f'Количество букв: {letter_count}')
     else:
        print('Invalid input type. Please provide a tuple, list or integer.')

if __name__=='__main__':
     function([1,2,3,'a','bc8?'])
     function((1,2,3,'a','bc8?',7,8,9))
     function(788)
     function('7fj88')
     function({1,2,3,4,5})







