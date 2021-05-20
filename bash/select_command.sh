#!/usr/bin/bash

# You can create ready-made textual option menus with the select command.
# Run this script and see this example


# define menu list
select brand in Samsung Sony Iphone HuaWei LG; do
    echo "you have chosen: $brand"
done


