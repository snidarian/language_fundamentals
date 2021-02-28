# This function can be useful if a process needs to determine who is running it before it runs
# Using $EUID which displays end user ID

check_root()
{
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root"
  exit 1
else
  # echo "you are root"
  ;
fi
}

# variation of above function checks if user is standard user
check_if_standard_user()
{
if [[ $EUID -eq 1000 ]]; then
# echo "You are standard user
;
else
# you are not standard user
;
fi
}



