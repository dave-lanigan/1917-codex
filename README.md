# Website and REST API for the 1917 Code of Canon Law [in development]

This [website](http://iudicabit.mywire.org) allows for the display and searchability of the 1917 Codex. There is also an API used to design the website and openn to help distribute the Codex's contents.


### Root endpoint (temporary):

www.iudicabit.mywire.org/api/v0/

### Public Endpoints:

##### /codex

(GET) Returns the entire codex in json format

Ex. Response:

```
{"book-1_general-principles-of-canon-law": {"canon-1": "It is stated in the first Canon of the Code that its laws...
```

##### /codex/(book)

(GET) Returns the entire book in json format. Possible route endings include: book-1,book-2,book-3,book-4,book-5

```
Ex: GET /codex/book-1
```
```
{"canon-1": "It is stated in the first Canon of the Code that its laws...
```
