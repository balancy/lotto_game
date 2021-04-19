# Lotto game

Script represents lotto game.

It's possible to choose the number of players and their type: human and computer.

Rules: 
1. Game continues while players has numbers in their cards.
2. Player wins if it has an empty card.
3. Human player loses if he chose to cross out the number while it hasn't it in his card, or he chose to continue 
   while he has the number to cross out.
   
4. Computer always crosses out the number if it's in his card

### How to install locally

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/lotto_game
```

2. Go inside cloned repository and create virtual environment by command:
```console
python -m venv env
```

3. Activate virtual environment. For linux-based OS:
```console
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;
For Windows:
```console
env\scripts\activate
```

## How to use

You run the script by command:

```console
python main.py
```
and follow the instructions.

## How to build and run via Docker

You create docker container by command:
```console
docker build -t lotto .
```

You run the container by command:
```console
docker run --rm -ti lotto
```