from django.shortcuts import render
import random

   
def code_gen():
    """
    This Function Generate code
    """
    code = []
    while len(code) != 4:
        digit = random.randint(0,9)
        if digit not in code:
            code.append(str(digit))

    return code



# Create your views here.
def game_home(request):
    
    return render(request,"mastermind/home.html",{
        "code":code_gen(),

    })
