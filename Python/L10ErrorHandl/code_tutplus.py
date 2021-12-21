"""
In this tutorial you'll learn how to handle error conditions in Python from a whole system point of view.
Error handling is a critical aspect of design, and it crosses from the lowest levels (sometimes the hardware) all the way to the end users. 
If you don't have a consistent strategy in place, your system will be unreliable, the user experience will be poor, and you'll have a lot of challenges debugging and troubleshooting. 

The key to success is being aware of all these interlocking aspects, considering them explicitly, and forming a solution that addresses each point.

Status Codes vs. Exceptions
There are two main error handling models: status codes and exceptions. Status codes can be used by any programming language. Exceptions require language/runtime support. 

Python supports exceptions. Python and its standard library use exceptions liberally to report on many exceptional situations like IO errors, divide by zero, out of bounds indexing, 
and also some not so exceptional situations like end of iteration (although it is hidden). Most libraries follow suit and raise exceptions.

That means your code will have to handle the exceptions raised by Python and libraries anyway, so you may as well raise exceptions from your code when necessary and not rely on status codes.

Quick Example
Before diving into the inner sanctum of Python exceptions and error handling best practices, let's see some exception handling in action:
"""
def f():
 
    return 4 / 0
 
 
 
def g():
 
    raise Exception("Don't call us. We'll call you")
 
 
 
def h():
 
    try:
 
        f()
 
    except Exception as e:
 
        print(e)
 
    try:
 
        g()
 
    except Exception as e:
 
        print(e)



"""
Python Exceptions
Python exceptions are objects organized in a class hierarchy. 

Here is the whole hierarchy:

BaseException
 
 +-- SystemExit
 
 +-- KeyboardInterrupt
 
 +-- GeneratorExit
 
 +-- Exception
 
      +-- StopIteration
 
      +-- StandardError
 
      |    +-- BufferError
 
      |    +-- ArithmeticError
 
      |    |    +-- FloatingPointError
 
      |    |    +-- OverflowError
 
      |    |    +-- ZeroDivisionError
 
      |    +-- AssertionError
 
      |    +-- AttributeError
 
      |    +-- EnvironmentError
 
      |    |    +-- IOError
 
      |    |    +-- OSError
 
      |    |         +-- WindowsError (Windows)
 
      |    |         +-- VMSError (VMS)
 
      |    +-- EOFError
 
      |    +-- ImportError
 
      |    +-- LookupError
 
      |    |    +-- IndexError
 
      |    |    +-- KeyError
 
      |    +-- MemoryError
 
      |    +-- NameError
 
      |    |    +-- UnboundLocalError
 
      |    +-- ReferenceError
 
      |    +-- RuntimeError
 
      |    |    +-- NotImplementedError
 
      |    +-- SyntaxError
 
      |    |    +-- IndentationError
 
      |    |         +-- TabError
 
      |    +-- SystemError
 
      |    +-- TypeError
 
      |    +-- ValueError
 
      |         +-- UnicodeError
 
      |              +-- UnicodeDecodeError
 
      |              +-- UnicodeEncodeError
 
      |              +-- UnicodeTranslateError
 
      +-- Warning
 
           +-- DeprecationWarning
 
           +-- PendingDeprecationWarning
 
           +-- RuntimeWarning
 
           +-- SyntaxWarning
 
           +-- UserWarning
 
           +-- FutureWarning
 
  +-- ImportWarning
 
  +-- UnicodeWarning
 
  +-- BytesWarning
  




   There are several special exceptions that are derived directly from  base exeption , like  SystemExit , KeyboardInterrupt  and  GeneratotExit. There is
   the  Exeption class for StopIteration , StandardError and Warning . All the standard errors are derived from  StandardError . 
   
   When you raise an exception or some function you called raises an exception, that normal code flow terminates and the exception 
   starts propagating up the call stack until it encounters a proper exception handler. 
   If no exception handler is available to handle it, the process (or more accurately the current thread) will be terminated with an unhandled exception message.
  """

  # Raise an instance of the Exception class itself
 
# raise Exception('Ummm... something is wrong')
 
 
 
# Raise an instance of the RuntimeError class
 
# raise RuntimeError('Ummm... something is wrong')
 
 
 
# Raise a custom subclass of Exception that keeps the timestamp the exception was created
 
from datetime import datetime
 
 
 
class SuperError(Exception):
 
    def __init__(self, message):
 
        Exception.__init__(message)
 
        self.when = datetime.now()
 
 
 
 
 
raise SuperError('Ummm... something is wrong')