# param_addition_detector
param_addition_detector.py is a program which analyzes all commits in a Java repository and find those commits that have added parameters to existing methods.

## Table of contents
* **[Requirements](#requirements)**
* **[Run Code](#run-code)**
* **[Other Info](#Other-Info)**
* **[Tested On Repositories](#tested-on-repositories)**


## REQUIREMENTS
Very few! Just:

- Python3
- Git

The list of dependencies is shown in `./requirements.txt`, however the installer takes care of installing them for you.

Install the requirements:

```
$ pip install -r requirements.txt
```


## RUN CODE
If you like to run the code on your machine , you can do it with very simple steps.

```
$ git clone https://github.com/kanfspfsp/param_addition_detector.git
$ python3 param_addition_detector.py

Enter relative path to the repository:
> /Users/kanfspfsp/Desktop/Git/Activiti
Enter the name of the output csv file
> ActivitiOut.csv
.....
```

## OTHER INFO
I have used Pydriller to mine through Git Software repositories. (https://github.com/ishepard/pydriller)

The file param_addition_detector.py has all the logic to detect the addition of params on existing methods. It is commented to understand the logic.



## TESTED ON REPOSITORIES

Activiti Workflow: https://github.com/Activiti/Activiti   -
> Report: ActivitiOut.csv (https://github.com/kanfspfsp/param_addition_detector/blob/master/ActivitiOut.csv)

Mockito Framework: https://github.com/mockito/mockito
> Report: mockitoOut.csv (https://github.com/kanfspfsp/param_addition_detector/blob/master/mockitoOut.csv)

RxJava- Reactive Extensions: https://github.com/ReactiveX/RxJava
> Report: ReactiveXOut.csv (https://github.com/kanfspfsp/param_addition_detector/blob/master/ReactiveXOut.csv)

