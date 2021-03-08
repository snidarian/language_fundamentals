#! /bin/bash

# This is by far the best spinning bash



# Bash, with GNU sleep                                                                                   
spin() {
  local i=0
  local sp='/-\|'
  local n=${#sp}
  printf ' '
  sleep 0.1
  while true; do
    printf '\b%s' "${sp:i++%n:1}"
    sleep 0.1
  done
}



spin





