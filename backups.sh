
#touch backup.sh

#sudo chmod 755 backup.sh
#nano backup.sh 

#!/bin/bash   


DAY="$(date +%Y_%m_%d)"                                                       
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"                             
tar -csvpzf $BACKUP /home/$USER/CompanyA

//Run the script: ./backup.sh
