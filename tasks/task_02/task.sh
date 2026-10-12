#!/usr/bin/env bash

# Перевірка кількості аргументів (має бути рівно 1)
if [ "$#" -ne 1 ]; then
    echo "Використання: task.sh ФАЙЛ" >&2
    exit 2
fi

FILE="$1"

# Перевірка, чи файл існує і є звичайним файлом
if [ ! -f "$FILE" ]; then
    echo "Помилка: файл не існує" >&2
    exit 3
fi

# Фільтрація користувачів: UID >= 1000, оболонка не закінчується на nologin або false
# Поля у /etc/passwd: 1-ім'я, 2-пароль, 3-UID, 4-GID, 5-коментар, 6-дім. каталог, 7-оболонка
awk -F: '$3 >= 1000 && $7 !~ /nologin$/ && $7 !~ /false$/ {print $3, $1}' "$FILE" | sort -k1,1n -k2,2 | awk '{print $2}' > /tmp/task02_res

# Виведення результату
if [ ! -s /tmp/task02_res ]; then
    echo "Немає"
else
    cat /tmp/task02_res
fi

rm -f /tmp/task02_res
exit 0