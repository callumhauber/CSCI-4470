# Lab 09 - Databases

## Checkpoint 0
https://github.com/callumhauber/CSCI-4470/wiki/Lab-9-Checkpoint-0

## Checkpoint 1
<img src="./screenshots/checkpoint1.png" width="700"/>

## Checkpoint 2
### 1.6.1
<img src="./screenshots/checkpoint2_1.png" width="700"/>

### 1.6.2
<img src="./screenshots/checkpoint2_2.png" width="700"/>

### 1.6.3
<img src="./screenshots/checkpoint2_3.png" width="700"/>

### 1.6.4
<img src="./screenshots/checkpoint2_4_1.png" width="700"/>

<img src="./screenshots/checkpoint2_4_2.png" width="700"/>

### 1.6.5
<img src="./screenshots/checkpoint2_5_1.png" width="700"/>

<img src="./screenshots/checkpoint2_5_2.png" width="700"/>

## Checkpoint 3
### 1.7.1
<img src="./screenshots/checkpoint3_1.png" width="700"/>

### 1.7.2
<img src="./screenshots/checkpoint3_2.png" width="700"/>

### 1.7.3
<img src="./screenshots/checkpoint3_3_1.png" width="700"/>

<img src="./screenshots/checkpoint3_3_2.png" width="700"/>

### 1.7.4
<img src="./screenshots/checkpoint3_4.png" width="700"/>

## Checkpoint 4
### Part 1
<img src="./screenshots/checkpoint4_1.png" width="700"/>

### Part 2
#### Command
```bash
curl -X POST admin:password@localhost:5984/hello-world/_find -d '{
   "selector": {
      "title": {
         "$gt": "L"
    }
  }
}' -H 'Content-Type: application/json'
```
<img src="./screenshots/checkpoint4_2.png" width="700"/>

### Part 3
<img src="./screenshots/checkpoint4_3.png" width="700"/>

### Part 4
#### Command
```bash
curl -X POST admin:password@localhost:5984/hello-world/_index -d '{
   "index": {
      "fields": [
         "title"
      ]
   },
   "name": "title-json-index",
   "type": "json"
}' -H 'Content-Type: application/json'
```
<img src="./screenshots/checkpoint4_4.png" width="700"/>