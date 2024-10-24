
"""

- Customizing Subclasses: Use __init_subclass__ to enforce certain criteria or to perform specific initializations when subclasses are created.
- Avoiding Repetitive Code: If you find yourself repeating code in subclasses, consider moving it to __init_subclass__ in the base class.
- Subclass Registration: Automatically register or track subclasses in applications like plugins or frameworks.

"""


class Base:
    # Using __init_subclass__ to ensure all subclasses have a required attribute
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'REQUIRED_ATTR'):
            raise AttributeError(f"{cls.__name__} must have 'REQUIRED_ATTR' attribute")

class SubClass1(Base):
    REQUIRED_ATTR = "I have this required attribute"

class SubClass2(Base):
    pass  # This will raise an error

# Usage
try:
    instance1 = SubClass1()  # This will succeed
    instance2 = SubClass2()  # This will raise an AttributeError
except AttributeError as e:
    print(e)  # Output: SubClass2 must have 'REQUIRED_ATTR' attribute