# Example Mapping

Example Mappings are workshops that help teams to create well defined user stories (small, specific). Example Mapping acts like a filter, preventing big fat stories from getting into your sprint and exploding with last-minute surprises three days before demo-day.

![](images/example-mapping.png)


**Acceptance Tests** and **Example Mapping** at the Socrates Converence 2019: [more details](Socrates-Conference.md)

source:
https://cucumber.io/blog/example-mapping-introduction/

# Feature Examples

**Behavior-Driven Development** (BDD) is an Agile software development process that encourages collaboration between developers, QA and business participants in a software project.

The **Three Amigos** define feature files:
* Developer (DEV)
* Tester (QA)
* Product Owner (PO)

Example feature file, `computer_search.feature`:
![](images/feature.png)

BDD aims to narrow the communication gaps between team members, foster better understanding of the customer and promote continuous communication with real world examples.

* express problems using the language of the domain stakeholders
* this language is then bound to code

Stakeholders often don’t actually create the scenarios, but developers usually do.

**Let behaviour drive your software architecture**

Imagine you see your system as a black box and design all acceptance tests from an outside perspecitve:

* all past PBIs are verified in each software build
* refactor software without breaking the system
* be the first customer of your software (black-box tests)
* it's like better user experience (UX), in this case on an API level
* make your system more accessible by providing the right API endpoints for easier testing

This black-box driven developent process ultimatively leads to a better software architecture.

## So let's get started

```
# start docker container
cd src/ComputerSearch
docker build --tag computer-search .
docker run -it -p 8001:80 computer-search

# execute acceptance tests
pipenv install
pipenv shell
cd features/computer_search
behave
```



The output:
![](images/behave.png)



## libraries and tools

pipenv (python package manager):
* https://github.com/pypa/pipenv

requests (REST library):
* https://2.python-requests.org/en/master/

behave:
* https://github.com/behave/behave
* https://github.com/behave/behave.example


PyHamcrest (assert library):
* https://github.com/hamcrest/PyHamcrest



## setup python and tools


```
pip install pipenv
```


install 'pipenv'
https://stackoverflow.com/a/51278649/5011904

error: The term 'pipenv' is not recognized as the name of a cmdlet, function, script file, or operable program.
https://stackoverflow.com/a/47676529/5011904
