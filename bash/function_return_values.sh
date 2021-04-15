#!/usr/bin/bash

# In bash there are no conventional return variables from function and so there are several methods to return values from functions:

# some example variable to use in the script
input_string="Some string"
input_integer=45


# 1st method - Allow the function to modify a global variable.
return_method_one()
{
    # 'process done to generate the variable'
    global_variable="Value you want to return"
}

return_method_one
# You would see the changes wrought on the variable by the function after its calling here.
echo $global_variable


# The problem with method one is obvious - Using global variables is not a wise course of action commonly (especially in large programs)

#----------------------------------------------------------------------------------------------------------------------------------------------

# 2nd method - set a local variable in the function and use echo command and command substitution to put its value into an outside variable

return_method_two()
{
    
    local local_variable='some value'
    # (some process done to string presumably)
    echo "$local_variable"
}

result_method_two=$(return_method_two) # You can also use command backticks `` for this.
echo "$result_method_two"

# The 2nd method is not a bad way to accomplish the aproximation of return values however to does still involve the creation of a global variables
# An important this to note, however is that in bash when a variable is created, it is, by default, a global variable

#----------------------------------------------------------------------------------------------------------------------------------------------

# 3rd method - passing an argument on a function call that is modified by the function itself

return_method_three()
{
    # create local variable and set equal to the first argument passed to the function
  #  local __resultvar=$1
 #   local myresult='some value'
    #    eval $__resultvar="'$myresult'"

}


#Create a value to pass to the function
    
return_method_three $result_method_three
echo $result_method_three


#----------------------------------------------------------------------------------------------------------------------------------------------

# This is the way that I prefer to write functions with return variables at my current skill leve
echo "prefer method results..."

prefer_method()
{
    local inputvar=$1
    #process that modifies string
    local resultvar=$inputvar
    echo $resultvar
}




input="string"

result=$(prefer_method $input)

echo=$result





