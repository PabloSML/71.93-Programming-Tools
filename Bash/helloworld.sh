#!/usr/bin/bash

# I am a comment! Hi :)

greet="Hello $1!"
user=$(whoami)
today=$(date)

echo $greet
sleep 2
echo "I'm $user"
sleep 2
echo "Today is $today"
sleep 2

while true; do
	read -p "Would you like some ice cream? " yn
	case $yn in
		[Yy]* ) break;;
		[Nn]* ) exit;;
		* ) echo "Please answer yes or no.";;
	esac
done

echo "Awesome! Here's some ice cream!"

read -p "On a scale of 1 to 10, how much fun is this? " appreciation
if [ $appreciation -lt 10 ] ; then
	echo "You can come back when you learn to appreciate art."
else
	echo "I knew you were cool :)"
fi
