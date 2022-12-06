# ECSE 211: Design Principles and Methods

## Team Information

__Team:__ 3  

__Members:__
- David Breton - 260986087
- Mathieu Geoffroy - 260986559
- Theo Ghanem - 260972584
- Sabrina Mansour - 260945807
- Sehr Moosabhoy - 260983946
- Ryan Reszetnik - 260948454


__DPM Kits:__ 05 and 06

## Project Files

### Mini Project
Our __mini project__ lab 3 code can be found at `/miniproject/LAB3/`.

To run the code:
```bash
python3 main.py
```

### Final Project
Our __final project__ code can be found at `/finalproject/project/`.

To run the code:
```bash
python3 main.py
```
The following arguments can be applied:  
| Argument | Action| Description |  
|:--------:|:-----:|-------------|
| -v | Verbose | Adds additional terminal print statements to understand the state of the program and the decision making. | 
| -d | Debug   | Enter inputs in the terminal instead of through the touch sensors on the BrickPi. |  
| -p | Preloaded Grid   | Use preloaded grid in code, instead of having to input data |  
  


## Setup

Below is setup information to connect to BrickPi #05. Changing the 5 for a 6 in the commands will do the same for BrickPi #06.  

__Note:__ To interact with the BrickPi, connect to its wifi.

### Connecting to the BrickPi

In your computer's terminal, run the following:
```bash
ssh pi@dpm-05.local
```
When prompted for a password, enter: `robots1234`


### Adding the BrickPi as a git remote
In your git repository, run the following on your computer's terminal:
```bash
git add remote brick5 pi@dpm-05.local:ecse211
```
Additionally, you can verify your remotes:
```bash
git remote -v
```


## Resetting the Repository (All on the BrickPi)

Remove the current repositoy on the BrickPi  

```bash
rm -rf ecse211
```


On the BrickPi, remake the directory:

```bash
mkdir ecse211
```

In the `ecse211` folder, intialize the repository:  

```bash
git init
```

Update the receiving configurations:

```bash
git config receive.denyCurrentBranch updateInstead
```

**On your computer:** push the repository to the robot:
```bash
git push brick5 main
``` 

If the repository does not appear, the robot may be on a wrong branch. Switch to main:  

```bash
git checkout main
```



