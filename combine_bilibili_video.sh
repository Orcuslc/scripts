cat /dev/null > ff.txt

for i in `ls -1 *.blv | sort -n`
    do echo "file '${i}'" >> ff.txt
done

ffmpeg -f concat -i ff.txt -c copy ../output.mp4

rm ff.txt
printf "success"
