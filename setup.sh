

prefix=$1

setup_list=("A" "B" "C" "D" "E")

for i in "${setup_list[@]}"; do
    name="${prefix}_${i}.py"
    cp template.py $name 
done