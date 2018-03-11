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
$ pip3 install -r requirements.txt
```

## Testing

```bash
$ pip3 install -r requirements-test.txt
$ pytest
```

## Patterns

### ABC Usage

Simple ABC usage scenario.
* `Runnable` – is an interface with methods `run`, `stop` and property `is_running`.
* `BadClass` – the class that inherited from Runnable, but does not implement it's methods/property.
* `GoodClass` – the class that fully implements Runnable interface.

### Strategy

Strategy pattern implementation. It allows you to encapsulate algorithms into the absolutely separated objects.

In this example we need to calculate Order shipping cost, that depends on shipping type: postal, FedEx, UPS.
* `Order` – just an empty class, that represents real order.
* `ShippingCost` – context, that contains selected shipping strategy.
* `Strategy` – abstract strategy with the only method `calculate(order: Order)`.
* `FedExStrategy`, `PostalStrategy`, `UPSStrategy` – implementations of concrete shipping strategies.

### Observer

Classic observer pattern implementation located in `observer.lib` package.
* `observer.lib.Observer` – abstract observer class
* `observer.lib.Subject` – abstract subject class with implemented default behavior 

In the example we have some "source" – `KPIs`, that is a `Subject` descendant. Also
we have two observers: `ClosedTickets` and `KPIsDisplay`. When the `KPIs` changes, it
notifies observers instances and they do their job.
* `KPIs` – event source, subject
* `ClosedTickets` – observer, calculates (and prints) the sum of total closed tickets
* `KPIsDisplay` – observer, just displays the current KPIs every time `update` is fired.

### Command

Command pattern with commands auto-discovery and fallback to NoCommand if there is no available command.

* `command.commands.*` – contains custom available commands.
* `command.executor.CommandExecutor` – the class, that is able to discovery and execute commands.
* `command.command.Command` – abstract console command.
* `command.no_command.NoCommand` – fallback command, that will be executed if no other command found.

### Singleton

Two implementations of Singleton pattern.

* `singleton.singleton_base.SingletonBase` – singleton, implemented as a base class.
* `singleton.singleton_meta.SingletonMeta` – singleton, implemented as a meta class.

### Builder

In this example, we need to build computers with different configurations.

* `builder.computer.Computer` – computer that we build.
* `builder.computer_builder.ComputerBuilder` – abstract computer builder.
* `builder.default_computer_builder.DefaultComputerBuilder` – default computer configuration.
* `builder.cheap_computer_builder.CheapComputerBuilder` – cheap computer configuration.
* `builder.director.Director` – director, the class, that knows how to build a computer.