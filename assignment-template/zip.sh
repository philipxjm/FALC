#!/bin/bash
echo Running zip script
echo CS Login \(e.x.: jx24\):
read cslogin
rm -f hw0_${cslogin}.zip
zip -r hw0_${cslogin}.zip . -x "*.git*" "*datasets*" "*.ipynb_checkpoints*" "*README.md" "*submit.sh" "*requirements.txt" ".env/*"
echo
echo
echo Zip script finished, email hw0_${cslogin}.zip to brown.cs147@gmail.com with the subject \"hw0\"
