from typing import Optional


class Bar:
    @property
    def get_foo(self):
        foo: Foo = Foo().save()
        return 1


class Foo:
    def save(self):
        return self
