
"""

- Customizing Subclasses: Use __init_subclass__ to enforce certain criteria or to perform specific initializations when subclasses are created.
- Avoiding Repetitive Code: If you find yourself repeating code in subclasses, consider moving it to __init_subclass__ in the base class.
- Subclass Registration: Automatically register or track subclasses in applications like plugins or frameworks.

"""


class Base:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        """Automatically called when a subclass is created."""
        super().__init_subclass__(**kwargs)
        Base.subclasses.append(cls)
        # Additional subclass initialization can go here
        cls.subclass_attribute = kwargs.get('subclass_attribute', None)

class SubClass1(Base, subclass_attribute="Value1"):
    pass

class SubClass2(Base, subclass_attribute="Value2"):
    pass

# Usage
print(Base.subclasses)  # [<class '__main__.SubClass1'>, <class '__main__.SubClass2'>]
print(SubClass1.subclass_attribute)  # Value1
print(SubClass2.subclass_attribute)  # Value2