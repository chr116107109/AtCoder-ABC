

prefix=$1

if [ -z "$prefix" ]; then
    echo "Usage: setup.sh <prefix>"
    exit 1
fi

setup_list=("A" "B" "C" "D" "E")

for i in "${setup_list[@]}"; do
    name="${prefix}_${i}.py"
    cp template.py $name 
done