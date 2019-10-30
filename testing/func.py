import re

def add_two(x,y):
    if isinstance(x, str) and x.isdigit():
        x = int(x)
    if isinstance(y, str) and y.isdigit():
        y = int(y)
    
    if isinstance(x, str) or isinstance(y, str):
        return None
        
    return x + y
    
# return true if the email is valid
def check_valid_email(address):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,address)):  
        return True 
          
    else:  
        return False 
    # if address.count("@") == 1 and address.count('.') > 0 and len(address) - address.rfind('.') >= 3:
    #     return True
    # return False
    
def calculate_gst(total):
    return 0.07 * total