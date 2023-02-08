
# C&C Malware

This malware makes requests HTTP to an API made in flask that stores the commands and responses that works as a server.

This code was made in order to study how malware of this type works, any illegal use of this content will be at your own risk.

## Autores

- [@exploit-py](https://www.github.com/exploit-py)


## Suporte

Contact me: gabriel.passos.dev@gmail.com

# Screenshots

## Hacker

![App Screenshot](https://cdn.discordapp.com/attachments/933791098827059204/1072775469532975134/image.png)

## Server (API)
![App Screenshot](https://cdn.discordapp.com/attachments/933791098827059204/1072775778879676506/8a3235db-94bf-4575-a5d8-7fda134db951.png)


## Deploy

Install requirements

```python
  pip install -r requirements.txt
```

Run server

```python
  python server_api.py
```

Run attacker

```python
  python attacker.py
```

Run victim

```python
  python victim.py
```


## Related

[CommandControl TCP](https://github.com/Exploit-py/Command-Control-TCP)


## Stacks


**Back-end:** Flask, Python

