
shopping_list = []

def add_item(item: str):

    shopping_list.append(item) 
    shopping_list.sort()  
def remove_item(item: str):

    index = binary_search(item)
    if index != -1:
        shopping_list.pop(index)  
    else:
        print(f"Item '{item}' not found in the shopping list.")

def binary_search(item: str) -> int:
   
    left, right = 0, len(shopping_list) - 1      
    while left <= right:
        mid = (left + right) // 2  
        if shopping_list[mid] == item:
            return mid 
        elif shopping_list[mid] < item:
            left = mid + 1  
        else:
            right = mid - 1 
    
    return -1  

def search_item(item: str) -> bool:

    return binary_search(item) != -1  

def display_list():

    if shopping_list: 
        print("Current Shopping List:")
        for idx, item in enumerate(reversed(shopping_list), start=1):
            print(f"{idx}. {item}") 
    else:
        print("The shopping list is currently empty.") 


if __name__ == "__main__":
    add_item("Milk")       
    add_item("Bread")      
    add_item("Eggs")       
    add_item("Apple")     
    
    display_list()        

    remove_item("Bread")  
    
    display_list()         

    found = search_item("Milk") 
    print(f" 'Milk' found {found}")


    remove_item("Bananas") 

    display_list()         
