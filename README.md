# python-orm
Testing python ORMs and DBs 

## docker
```
docker-compose up -d
```

## development
First config:
```
python3 -m venv env
source env/bin/activate
pip3 install -r ./app/requirements.txt
```

Update ´requirements.tx´:
```
source env/bin/activate
pip3 install package
pip3 freeze > requirements.txt
```
Update docker image:
```
docker-compose up --build -d
```