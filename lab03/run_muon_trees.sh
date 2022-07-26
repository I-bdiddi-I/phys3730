#nmax=2000001
#sleep 3h
nmax=99999
nstart=300002
for i in $( ls -1d tree*.root ); do

    id=` echo $1  | awk -F"." '{print $1}' | awk -F"tree" '{print $2}'`
    echo 
