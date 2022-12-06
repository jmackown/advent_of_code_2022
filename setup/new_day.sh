day=$1

touch "puzzles/input_data/day${day}.txt"
touch "tests/data/day_${day}.txt"

cp "setup/day.py" "puzzles/day_${day}.py"
sed -i "" "s/{{day}}/$day/g" "puzzles/day_${day}.py"

cp "setup/test_day.py" "tests/test_day_${day}.py"
sed -i "" "s/{{day}}/$day/g" "tests/test_day_${day}.py"

