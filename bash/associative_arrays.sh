#!/usr/bin/bash


# -A argument specifies and associative array declaration
declare -A aa




# Variable assignments are made by putting a key inside square brackets and
# then assigning it to the corresponding value
aa[key0]=value0
aa[key1]=value1
aa[key2]=value2
aa[key3]=value3
aa[key4]=value4
aa[key5]=value5
aa[key6]=value6
aa[key7]=value7
aa[key8]=value8
aa[key9]=value9
aa[key10]=value10
aa[key11]=value11
aa[key12]=value12
aa[key13]=value13
aa[key14]=value14
aa[key15]=value15
aa[key16]=value16
aa[key17]=value17
aa[key18]=value18
aa[key19]=value19
aa[key20]=value20
aa[key21]=value21
aa[key22]=value22
aa[key23]=value23
aa[key24]=value24


# using the values in the associative array
# use in the following format ${associative_array[key]} 

echo ${aa[key0]}


# you can print all the values in an associative array by using '@' as the key
echo ${aa[@]}

# an value in an associative array can be another variable like with value25
value25="heyhowsitsgoing"

aa[key25]=$value25 # key25 references a variable that contains a string

# This prints the contents of the $value25 variable of the aa array at [key25]
echo "${aa[key25]}"


# declaring multiple values at once
# The below method erases all other key-values other than 26 and 27
# aa=([value26]="value26" [value27]="value27")
# you can use the += operator to add a key-value to the associative array
aa+=(["value-1"]="value-1")

# control flow using associative array items

if [[ ${aa[key24]} == "value24" ]]; then
    echo "testsuccess"
else
    echo "testfail"
fi


# the key itself can be a string and can contain spaces (if using double quotes)

aa["string key28"]="string value 28"

echo ${aa["string key28"]}



# you can use a for loop to iterate over all the values in 'aa'

# Notice the difference when ${aa[@]} is quoted or not
# it prints strings with spaces in them as separate line values
for loopvar in "${aa[@]}"
do
    echo $loopvar
done

echo "---------------------------------------"

# You can also extend associative arrays with the += operator


aa+=([value29]="value29")






echo "${aa[@]}"
