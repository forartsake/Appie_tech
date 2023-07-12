# Task1

## CSV File Combiner

This script allows you to merge two CSV files based on the current date value in the 'update' field and saves the result to a new CSV file. 
Please note that the value of the 'update' column will be replaced with the current date.

## Requirements
- Python 3
 - Pandas Library

You can install dependencies with the command:
```shell
pip install -r requirements.txt
```


## Usage

Run the script as follows:

```shell
python main.py <file1.csv> <file2.csv> <output_file.csv>
```
Where:

- <file1.csv> is the path to the first input CSV file.
- <file2.csv> - path to the second input CSV file.
- <output_file.csv> - the path to the output CSV file where the merge result will be saved.



# Task2

## 1.

a) 

```shell
SELECT brand, model, COUNT(contract_id) AS popular_car
FROM cars
GROUP BY brand, model
ORDER BY purchase_count DESC
LIMIT 1;
```
b) 
```shell
SELECT brand, model
FROM cars
ORDER BY int DESC
LIMIT 1;
```
c) 
* Примечание: в БД нет полей с датами
```shell
SELECT brand, model, MONTH(sale_date) AS top_month
FROM cars
WHERE brand == "Kia" AND model == "Rio"
GROUP BY MONTH(sale_date)
ORDER BY sales_count DESC
LIMIT 1;
```

d) 
```shell
SELECT sum 
FROM cars
LIMIT 1 OFFSET 26;
```
## 2.

a) 

```shell
SELECT utm_term, COUNT(*) AS total_clients 
FROM sessions
WHERE utm_source == 'google'
GROUP BY utm_term
LIMIT 1;
```

b) 
```shell
SELECT yandex.utm_term
FROM
(
  SELECT utm_term
  FROM sessions
  WHERE utm_source = 'yandex'
  GROUP BY utm_term
  HAVING COUNT(*) > 20
) AS yandex
LEFT JOIN
(
  SELECT utm_term
  FROM sessions
  WHERE utm_source = 'google'
  GROUP BY utm_term
  HAVING COUNT(*) > 20
) AS google
ON yandex.utm_term = google.utm_term;
```

c) 

```shell
SELECT utm_campaign, COUNT(ClientID) as clients
FROM sessions
WHERE utm_source = 'facebook' AND DATETIME >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
GROUP BY utm_campaign
HAVING COUNT(ClientID) >= 20;
```
3) 
```shell
Премию получит Василий, при условии, что работники будут действовать рационально, 
т.е. каждый будет продавать авто с максимальной выгодой для компании (1 авто за 3 млн),
 то премию получит Василий. На момент продажи 21-го авто компанией,
Василий продаст 11 штук, а Алина -- 10.
```

4)
```shell
Первый вариант:
При наличии картельного сговора, первые три компании могут поделить квоты на автомобили между собой,
 т.к. достигают в 50% для принятия решения (тогда квоты будут разделены между 3-я компаниями пропорционально 
 их партфелю)
Второй вариант:
Разделение квот в зависимости от  размера портфелей компаний,
 т.к. в интересах каждой компании получить максимальное выгодное предложение для себя 
 с учетом интересов всех компаний, для достижения 50% согласия   
```

