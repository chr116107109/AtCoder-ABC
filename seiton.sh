

for file_name in $(ls .); do
    if [[ ${file_name} =~ ([0-9]+)_([A-Z])* ]]; then
        echo "Matched $file_name"
        number=${BASH_REMATCH[1]}
        echo "Number: $number"

        # dirがなければ作成
        if [ ! -d $number ]; then
            mkdir $number
        fi

        mv $file_name $number
    fi

done