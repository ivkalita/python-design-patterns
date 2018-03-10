# Design patterns in Python

This repository contains python implementations of common design patterns based on
[Design Patterns with Python](https://app.pluralsight.com/library/courses/python-design-patterns) course.

## Requirements

* Python 3.6+
* pip3

## Installation

```bash
$ git clone https://github.com/kaduev13/python-design-patterns.git
$ cd python-design-patterns
```

## Testing

```bash
$ pip3 install -r requirements-test.txt
$ pytest
```

## Modules

### ABC Usage

Simple ABC usage scenario.
* Runnable – is an interface with methods `run`, `stop` and property `is_running`.
* BadClass – the class that inherited from Runnable, but does not implement it's methods/property.
* GoodClass – the class that fully implements Runnable interface.

