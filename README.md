## Тестовый задание

### Запуск:  

```
docker-compose build
docker-compose up --remove-orphans -d --build
```

### Запуск web интерфейса 
http://localhost:9000/docs

### Используемые инструменты:
* Виртуальное окружение - poetry
* python 3.10
* FastApi 0.95.0
* pydantic 1.10.7

---

### Задание № 2
```
queryset = FullNames.objects.iterator(chunk_size=5_000)
data = []
number_request = 0
for qs in queryset:
    try:
        f_name = str(qs.name).split(".")[0]
    except IndexError:
        continue
    short_names = ShortNames.objects.filter(name=f_name).first()
    if short_names:
        qs.status = short_names.status
        data.append(qs)
    if number_request >= 5_000:
        FullNames.objects.bulk_update(data, "status")
        data = []
        number_request = 0

```

